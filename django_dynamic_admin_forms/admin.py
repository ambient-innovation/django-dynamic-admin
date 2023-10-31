import json
from itertools import filterfalse

from django.apps import apps
from django.contrib import admin
from django.core.exceptions import FieldDoesNotExist, PermissionDenied
from django.http import HttpResponse


class DynamicModelAdminMixin:
    dynamic_fields = ()
    dynamic_select_fields = None
    dynamic_input_fields = None

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, **{"change": change, **kwargs})
        self.dynamic_select_fields = list(filter(self._is_related_field, self.dynamic_fields))
        self.dynamic_input_fields = list(filterfalse(self._is_related_field, self.dynamic_fields))
        return form

    def _is_related_field(self, field_name):
        try:
            return self.opts.get_field(field_name).is_relation
        except FieldDoesNotExist:
            return False

    @staticmethod
    def render_field(request) -> HttpResponse:
        app_label = request.GET.get("app_label")
        model_name = request.GET.get("model_name")
        field_names = request.GET.getlist("field_names")

        if not (app_label and model_name and field_names):
            return HttpResponse("Invalid arguments", status=400)

        model = apps.get_model(app_label, model_name)

        # instantiate model_admin form from request data and get field
        model_admin = admin.site._registry[model]

        # check permissions
        if not model_admin.has_module_permission(request):
            raise PermissionDenied

        model_form = model_admin.get_form(request)
        bound_form = model_form(request.POST)

        snippets = []
        for field_name in field_names:
            bound_field = bound_form[field_name]

            # save custom queryset in field
            hidden = False
            method_name = f"get_dynamic_{field_name}_field"
            if hasattr(model_admin, method_name):
                method = getattr(model_admin, method_name)
                bound_form.full_clean()
                queryset, value, hidden = method(bound_form.cleaned_data)

                bound_field.field.queryset = queryset
                bound_field.form.data = bound_field.form.data.copy()
                bound_field.form.data[field_name] = value

            skip_update = field_name in request.FILES and not hidden
            html = bound_field.as_widget()

            snippets.append(
                {
                    "field_name": field_name,
                    "html": html,
                    "hidden": hidden,
                    "skipUpdate": skip_update,
                }
            )

        return HttpResponse(json.dumps(snippets), status=200)
