from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from assets.models import Company
from assets.serializers import CompanySerializer


class CompanyAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.company1 = Company.objects.create(name="Test Company 1")
        self.company2 = Company.objects.create(name="Test Company 2")

    def test_company_list(self):
        url = reverse("company-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_company_detail(self):
        url = reverse("company-detail", kwargs={"pk": self.company1.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Company 1")

        url = reverse("company-detail", kwargs={"pk": 1000})  # Non-existent pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
