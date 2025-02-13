from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def normalize_email(self, email):
        email = email or ''
        return email.lower()

    def create_user(self, email, company_name, password=None, **extra_fields):
        """View for creating users with validated email and password."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)

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
    nip = models.CharField(max_length=10, blank=True, null=True)  # NIP
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Numer telefonu
    company_address = models.TextField(blank=True, null=True)  # Adres siedziby firmy
    invoice_name = models.CharField(max_length=255, blank=True, null=True)  # Pełna nazwa firmy do faktury


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name']

    def __str__(self):
        return self.company_name
