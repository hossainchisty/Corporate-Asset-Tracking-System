from rest_framework import generics, permissions
from .models import Company, Employee, Device, DeviceLog
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
    DeviceSerializer,
    DeviceLogSerializer,
)


class CompanyList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Company instances.

    - GET: Retrieve a list of all companies.
    - POST: Create a new company instance.

    Inherits:
        - `ListCreateAPIView`: A generic class-based view for listing and creating objects.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting Company instances.

    - GET: Retrieve details of a specific company.
    - PUT: Update details of a specific company.
    - DELETE: Delete a specific company.

    Inherits:
        - `RetrieveUpdateDestroyAPIView`: A generic class-based view for retrieving, updating, and deleting objects.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Employee instances.

    - GET: Retrieve a list of all employees.
    - POST: Create a new employee instance.

    Inherits:
        - `ListCreateAPIView`: A generic class-based view for listing and creating objects.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting Employee instances.

    - GET: Retrieve details of a specific employee.
    - PUT: Update details of a specific employee.
    - DELETE: Delete a specific employee.

    Inherits:
        - `RetrieveUpdateDestroyAPIView`: A generic class-based view for retrieving, updating, and deleting objects.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Device instances.

    - GET: Retrieve a list of all devices.
    - POST: Create a new device instance.

    Inherits:
        - `ListCreateAPIView`: A generic class-based view for listing and creating objects.
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting Device instances.

    - GET: Retrieve details of a specific device.
    - PUT: Update details of a specific device.
    - DELETE: Delete a specific device.

    Inherits:
        - `RetrieveUpdateDestroyAPIView`: A generic class-based view for retrieving, updating, and deleting objects.
    """

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceLogList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating DeviceLog instances.

    - GET: Retrieve a list of all device logs.
    - POST: Create a new device log instance.

    Inherits:
        - `ListCreateAPIView`: A generic class-based view for listing and creating objects.
    """

    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting DeviceLog instances.

    - GET: Retrieve details of a specific device log.
    - PUT: Update details of a specific device log.
    - DELETE: Delete a specific device log.

    Inherits:
        - `RetrieveUpdateDestroyAPIView`: A generic class-based view for retrieving, updating, and deleting objects.
    """

    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]
