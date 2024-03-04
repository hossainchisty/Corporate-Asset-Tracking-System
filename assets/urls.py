from django.urls import path
from .views import (
    CompanyList,
    CompanyDetail,
    EmployeeList,
    EmployeeDetail,
    DeviceList,
    DeviceDetail,
    DeviceLogList,
    DeviceLogDetail,
)

urlpatterns = [
    path("companies/", CompanyList.as_view(), name="company-list"),
    path("companies/<int:pk>/", CompanyDetail.as_view(), name="company-detail"),
    path("employees/", EmployeeList.as_view(), name="employee-list"),
    path("employees/<int:pk>/", EmployeeDetail.as_view(), name="employee-detail"),
    path("devices/", DeviceList.as_view(), name="device-list"),
    path("devices/<int:pk>/", DeviceDetail.as_view(), name="device-detail"),
    path("devicelogs/", DeviceLogList.as_view(), name="devicelog-list"),
    path("devicelogs/<int:pk>/", DeviceLogDetail.as_view(), name="devicelog-detail"),
]
