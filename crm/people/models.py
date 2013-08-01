from django.db import models

from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)

class EmergencyContact(models.Model):

    RELATION_CHOICES = (
        ('Parent', 'Parent'),
        ('Child', 'Child'),
        ('Significant Other', 'Significant Other'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User)
    name = models.CharField(max_length=255, null=True, blank=True)
    relation = models.CharField(max_length=255, choices=RELATION_CHOICES, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.user.username + u' (%s)' % self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to="user_photos", blank=True, null=True)

    def __unicode__(self):
        return self.user.username
