from django.contrib import admin
from django import forms

from .models import Customer, District, Employee
from dynamic_admin_forms.admin import DynamicModelAdminMixin


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "district")


class CustomerForm(forms.ModelForm):
    some_text = forms.CharField(max_length=100)

    class Meta:
        model = Customer
        fields = ()


@admin.register(Customer)
class CustomerAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    form = CustomerForm
    fields = ("name", "district", "employee", "lead_reason", "lead_reason_other", "some_text")
    dynamic_fields = ("employee", "lead_reason_other", "some_text")

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

    def get_dynamic_some_text_field(self, data):
        value = data.get("name")
        return None, value, False
