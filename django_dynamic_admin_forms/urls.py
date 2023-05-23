from django.urls import path
from dynamic_admin_forms.admin import DynamicModelAdminMixin

urlpatterns = [
    path("", DynamicModelAdminMixin.render_field),
]
