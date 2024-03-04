from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from assets.models import DeviceLog, Company, Device, Employee
from assets.serializers import DeviceLogSerializer


class DeviceLogAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.company = Company.objects.create(name="Company 1")
        self.device = Device.objects.create(company=self.company, name="Device 1")
        self.employee = Employee.objects.create(user=self.user, company=self.company)
        self.device_log1 = DeviceLog.objects.create(
            device=self.device, checked_out_by=self.employee
        )
        self.device_log2 = DeviceLog.objects.create(
            device=self.device, checked_out_by=self.employee
        )

    def test_device_log_list(self):
        url = reverse("devicelog-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_device_log_detail(self):
        url = reverse("devicelog-detail", kwargs={"pk": self.device_log1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["device"], self.device.id)

        url = reverse("devicelog-detail", kwargs={"pk": 1000})  # Non-existent pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_devicelog_retrieve_nonexistent(self):
        url = reverse("devicelog-detail", kwargs={"pk": 1000})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_devicelog_delete(self):
        url = reverse("devicelog-detail", kwargs={"pk": self.device_log1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
