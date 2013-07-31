from django.db import models
from django.contrib.auth.models import User


class RFIDTag(models.Model):
    tag = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = 'RFID Tag'
        verbose_name_plural = 'RFID Tags'
