from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")

    is_patient = models.BooleanField(default=False)
    is_psychologue = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

class Psychologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='psychologue')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

class Text(models.Model):
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=200, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
