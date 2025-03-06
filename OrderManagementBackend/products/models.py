"""
Models for the 'products' app.
Defines Product and ProductTag models for the OrderManagement system.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductTag(models.Model):
    """Product tag model with a unique name."""
    name = models.CharField(
        _("name"),
        max_length=100,
        unique=True,
        error_messages={"unique": _("A tag with this name already exists.")},
    )

    class Meta:
        verbose_name = _("product tag")
        verbose_name_plural = _("product tags")

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model representing items available for order."""
    title = models.CharField(
        _("title"),
        max_length=120,
        blank=False,
        error_messages={"blank": _("Title cannot be empty.")},
    )
    description = models.TextField(_("description"))
    price = models.IntegerField(
        _("price"),
    )
    image = models.ImageField(
        _("image"),
        upload_to="products/images/",
        null=True,
        blank=True,
        default="products/images/PolishLodyLogo.jpg",
    )
    is_active = models.BooleanField(_("is active"), default=True)
    tags = models.ManyToManyField(
        "ProductTag",
        verbose_name=_("tags"),
        related_name="products",
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title
    
