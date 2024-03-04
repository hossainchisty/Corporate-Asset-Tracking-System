from django.db import models
from django.utils.timezone import now


class Timestamp(models.Model):
    """Abstract base model for create and update timestamp and user for all models."""

    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        abstract = True
