from django.contrib import admin

from .models import Customer, District, Employee
from dynamic_admin.admin import DynamicModelAdminMixin


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    fields = ("name", "has_middle_name", "middle_name", "district", "employee")
    dynamic_fields = ("name", "middle_name", "employee",)

    def get_dynamic_middle_name_field(self, data):
        if data.get("has_middle_name"):
            return None, data.get("middle_name"), False
        return None, None, True

    def get_dynamic_employee_field(self, data):
        queryset = Employee.objects.filter(district=data.get("district"))
        value = data.get("employee")

        if value not in queryset:
            value = queryset.first()

        hidden = False

        return queryset, value, hidden

    def get_dynamic_name_field(self, data):
        if name := data.get("name"):
            return None, name, False
        else:
            return None, data.get("district"), False


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
