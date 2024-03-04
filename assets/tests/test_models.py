from django.test import TestCase
from django.contrib.auth.models import User
from assets.models import Company, Employee, Device, DeviceLog


class ModelsTestCase(TestCase):
    def setUp(self):

        self.company = Company.objects.create(name="Test Company")

        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        self.employee = Employee.objects.create(user=self.user, company=self.company)

        self.device = Device.objects.create(company=self.company, name="Test Device")

        self.device_log = DeviceLog.objects.create(
            device=self.device,
            checked_out_by=self.employee,
            condition_on_checkout="Good",
            condition_on_checkin="Good",
        )

    def test_company_str(self):
        self.assertEqual(str(self.company), "Test Company")

    def test_employee_str(self):
        expected_str = f"{self.user.first_name} {self.user.last_name} ({self.company})"
        self.assertEqual(str(self.employee), expected_str)

    def test_device_str(self):
        expected_str = f"Test Device ({self.company})"
        self.assertEqual(str(self.device), expected_str)

    def test_device_log_str(self):
        expected_str = f"Log for Test Device checked out by {self.user.first_name} ({self.device_log.check_out_date})"
        self.assertEqual(str(self.device_log), expected_str)
