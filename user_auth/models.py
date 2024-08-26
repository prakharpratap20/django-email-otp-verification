from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    """
    Custom User Model with email and mobile number as unique fields
    and email and mobile number verification fields and otp fields.
    """
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    mobile_otp = models.CharField(max_length=6, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_user_permissions_set')
