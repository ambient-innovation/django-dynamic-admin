from unittest.mock import MagicMock

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import QueryDict
from django.test import RequestFactory, TestCase

from django_dynamic_admin_forms.admin import DynamicModelAdminMixin
from testapp.models import Customer


class MyDynamicModelAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    dynamic_fields = ["related_field"]

    def get_dynamic_related_field_field(self, cleaned_data):
        pass


class TestDynamicModelAdminMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
        # cls.mixin = DynamicModelAdminMixin()
        # cls.mixin.opts = site._registry[User]

    def get_request(self, is_superuser: bool):
        factory = RequestFactory()
        user = User.objects.create_user(username="testuser", password="testpassword", is_superuser=is_superuser)
        request = factory.get("/admin/")
        request.user = user

        return request

    def test_render_field_with_valid_arguments(self):
        # Test with valid arguments
        request = self.get_request(is_superuser=True)
        request.GET = QueryDict("app_label=auth&model_name=user&field_names=password1&field_names=password2")

        mixin = DynamicModelAdminMixin()
        response = mixin.render_field(request)

        self.assertEqual(response.status_code, 200)
        data = response.content.decode("utf-8")
        # Add further checks on the data in the response
        self.assertNotEqual(data, "")

    def test_render_field_with_custom_method(self):
        # Test with valid arguments
        request = self.get_request(is_superuser=True)
        request.GET = QueryDict("app_label=testapp&model_name=customer&field_names=employee")

        my_admin = MyDynamicModelAdmin(Customer, admin.site)

        my_admin.has_module_permission = MagicMock(return_value=True)
        my_admin.get_form = MagicMock()
        my_admin.get_form().full_clean = MagicMock()

        response = my_admin.render_field(request)

        self.assertEqual(response.status_code, 200)

    def test_render_field_with_missing_arguments(self):
        # Test with missing arguments
        request = self.get_request(is_superuser=True)
        request.GET = QueryDict("")

        mixin = DynamicModelAdminMixin()
        response = mixin.render_field(request)

        self.assertEqual(response.status_code, 400)
        data = response.content.decode("utf-8")
        self.assertEqual(data, "Invalid arguments")

    def test_render_field_with_permission_denied(self):
        # Test with missing permissions
        request = self.get_request(is_superuser=False)
        request.GET = QueryDict("app_label=auth&model_name=user&field_names=password1&field_names=password2")

        mixin = DynamicModelAdminMixin()

        # You can adjust the permissions for the user to raise PermissionDenied
        with self.assertRaises(PermissionDenied):
            mixin.render_field(request)
