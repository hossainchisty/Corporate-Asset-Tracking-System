from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.company})"


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.company})"


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    checked_in_by = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="checked_in_logs",
    )
    check_out_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_checkin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Log for {self.device.name} checked out by {self.checked_out_by.user.first_name} ({self.check_out_date})"
