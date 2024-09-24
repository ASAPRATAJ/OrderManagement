from django.db import models

tags = ['Podstawowa', 'Rozszerzona', 'Premium', 'Smaki tygodnia']


class Product(models.Model):
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
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

