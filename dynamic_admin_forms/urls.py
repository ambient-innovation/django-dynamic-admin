from django.urls import path

from dynamic_admin_forms.admin import DynamicModelAdminMixin

urlpatterns = [
    path("<app_label>/<model_name>/<field_name>/", DynamicModelAdminMixin.render_field),
]
