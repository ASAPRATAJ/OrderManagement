# accounts/models.py
import re
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def normalize_email(self, email):
        email = email or ''
        return email.lower()

    def validate_password(self, password):
        if len(password) < 8:
            raise ValueError(_('Password must contain at least 8 characters'))
        if not re.search(r'[A-Z]', password):
            raise ValueError(_('Password must contain at least one uppercase letter'))
        if not re.search(r'[a-z]', password):
            raise ValueError(_('Password must contain at least one lowercase letter'))
        if not re.search(r'\d', password):
            raise ValueError(_('Password must contain at least one digit'))
        if not re.search(r'[\W_]', password):  # \W matches any non-word character, including special characters
            raise ValueError(_('Password must contain at least one special character'))

    def create_user(self, email, company_name, password=None, **extra_fields):
        """View for creating users with validated email and password."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)

        self.validate_password(password)

        user = self.model(email=email, company_name=company_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, company_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, company_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name']

    def __str__(self):
        return self.company_name
