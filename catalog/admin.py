from django.contrib import admin

# Register your models here.
from .models import Department, Location, Employee

#admin.site.register(Employee)
#admin.site.register(Department)
admin.site.register(Location)

# Define the admin class
class DepartmentAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Department, DepartmentAdmin)

# Register the Admin classes for Employee using the decorator

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('Name', 'department')

  