from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextInputWidget

from django_dynamic_admin_forms.admin import DynamicModelAdminMixin

from .models import Customer, District, Employee


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "district")


class CustomerForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=100,
        required=False,
        widget=AdminTextInputWidget(attrs={"readonly": "true", "disabled": "true", "style": "border: none"}),
    )

    class Meta:
        model = Customer
        fields = ()


@admin.register(Customer)
class CustomerAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    form = CustomerForm
    fields = (
        "first_name",
        "last_name",
        "full_name",
        "district",
        "employee",
        "lead_reason",
        "lead_reason_other",
        "has_profile_picture",
        "profile_picture",
    )
    dynamic_fields = ("employee", "lead_reason_other", "full_name", "profile_picture")

    def get_dynamic_employee_field(self, data):
        queryset = Employee.objects.filter(district=data.get("district"))
        value = data.get("employee")

        if value not in queryset:
            value = queryset.first()

        hidden = False

        return queryset, value, hidden

    def get_dynamic_lead_reason_other_field(self, data):
        hidden = data.get("lead_reason") != Customer.LeadReason.OTHER
        if hidden:
            value = ""
        else:
            value = data.get("lead_reason_other")
        return None, value, hidden

    def get_dynamic_full_name_field(self, data):
        value = data.get("first_name", "") + " " + data.get("last_name", "")
        return None, value, False

    def get_dynamic_profile_picture_field(self, data):
        return None, None, not data.get("has_profile_picture")
