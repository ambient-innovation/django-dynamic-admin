from django.contrib import admin

from .models import Customer, District, Employee
from dynamic_admin_forms.admin import DynamicModelAdminMixin


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    fields = ("name", "district", "employee", "lead_reason", "lead_reason_other")
    dynamic_fields = ("employee", "lead_reason_other")

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


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "district")
