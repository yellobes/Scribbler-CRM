from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)

class EmergencyContact(models.Model):
    user = models.ForeignKey(User)
    name = models.EmailField(null=True, blank=True)
    address = models.EmailField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.EmailField(null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to="user_photos", blank=True, null=True)
