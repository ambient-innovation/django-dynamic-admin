from django.contrib import admin
from django.urls import path

from django_dynamic_admin_forms.admin import DynamicModelAdminMixin

urlpatterns = [
    path("", admin.site.admin_view(DynamicModelAdminMixin.render_field)),
]
