from django.db import models


class Product(models.Model):
    """Fields of Product Model in database"""
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', null=True, blank=True,
                              default='products/images/PolishLodyLogo.jpg')
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField('ProductTag')

    def __str__(self):
        return self.title


class ProductTag(models.Model):
    """Fields of ProductTag Model in database"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

