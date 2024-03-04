from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)
