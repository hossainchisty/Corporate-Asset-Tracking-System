from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from assets.models import Company, Device
from assets.serializers import DeviceSerializer


class DeviceAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.company = Company.objects.create(name="Company 1")
        self.device1 = Device.objects.create(company=self.company, name="Device 1")
        self.device2 = Device.objects.create(company=self.company, name="Device 2")

    def test_device_list(self):
        url = reverse("device-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_device_detail(self):
        url = reverse("device-detail", kwargs={"pk": self.device1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["company"], self.company.id)

        url = reverse("device-detail", kwargs={"pk": 1000})  # Non-existent pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_device_update(self):
        url = reverse("device-detail", kwargs={"pk": self.device1.pk})
        self.client.force_authenticate(user=self.user)
        data = {"company": self.company.id, "name": "Updated Device"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Device")

    def test_device_retrieve_nonexistent(self):
        url = reverse("device-detail", kwargs={"pk": 1000})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_device_delete(self):
        url = reverse("device-detail", kwargs={"pk": self.device1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
