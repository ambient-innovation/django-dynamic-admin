from django.urls import path

from django_dynamic_admin_forms.admin import DynamicModelAdminMixin

urlpatterns = [
    path("", DynamicModelAdminMixin.render_field),
]
