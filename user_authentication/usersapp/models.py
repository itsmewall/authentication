from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    jobTitle = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users_permissions'
    )
