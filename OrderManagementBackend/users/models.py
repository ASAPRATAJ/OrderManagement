"""
Models for the 'users' app.
Defines the custom user model and its manager for the OrderManagementBackend project.
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .validators import CustomPasswordValidator


class CustomUserManager(BaseUserManager):
    """Manager for the CustomUser model with email-based authentication."""

    def normalize_email(self, email):
        """Normalize email to lowercase, ensuring consistency."""
        return (email or "").lower()

    def create_user(self, email, company_name, password=None, **extra_fields):
        """Create and save a regular user with the given email and password."""
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, company_name=company_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, company_name, password=None, **extra_fields):
        """Create and save a superuser with elevated permissions."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(email, company_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model using email as the unique identifier."""

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )
    company_name = models.CharField(_("company name"), max_length=255)
    nip = models.CharField(
        _("NIP"),
        max_length=10,
        blank=True,
        null=True,
        validators=[RegexValidator(r"^\d{10}$", message="NIP must be exactly 10 digits.")],
    )
    phone_number = models.CharField(
        _("phone number"),
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(r"^\+?\d{9,15}$", message="Phone number must be 9-15 digits.")],
    )
    company_address = models.TextField(_("company address"), blank=True, null=True)
    invoice_name = models.CharField(_("invoice name"), max_length=255, blank=True, null=True)

    # Django-specific fields
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["company_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        """Return string representation of the user."""
        return self.company_name

    def set_password(self, password):
        validator = CustomPasswordValidator()
        validator.validate(password)
        super().set_password(password)

