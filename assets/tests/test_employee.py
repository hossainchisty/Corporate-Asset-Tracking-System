from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from assets.models import Company, Employee
from assets.serializers import EmployeeSerializer


class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.company = Company.objects.create(name="Company 1")
        self.employee1 = Employee.objects.create(user=self.user, company=self.company)

    def test_employee_list(self):
        url = reverse("employee-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_employee_detail(self):
        url = reverse("employee-detail", kwargs={"pk": self.employee1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.id)

        url = reverse("employee-detail", kwargs={"pk": 1000})  # Non-existent pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_employee_retrieve_nonexistent(self):
        url = reverse("employee-detail", kwargs={"pk": 1000})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_employee_update(self):
        url = reverse("employee-detail", kwargs={"pk": self.employee1.pk})
        self.client.force_authenticate(user=self.user)
        data = {"user": self.user.id, "company": self.company.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.user.id)

    def test_employee_delete(self):
        url = reverse("employee-detail", kwargs={"pk": self.employee1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
