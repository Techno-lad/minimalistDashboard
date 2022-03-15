from django.contrib import admin
from employeeDash.models import Employees,Supervisor

# Register your models here.

admin.site.register(Employees)
admin.site.register(Supervisor)