from django.db import models
from django.contrib.auth.models import User


class RFIDTag(models.Model):
    tag = models.CharField(max_length=255, unique=True, blank=False, null=False)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = 'RFID Tag'
        verbose_name_plural = 'RFID Tags'
