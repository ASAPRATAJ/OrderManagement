from django.db import models

tags = ['Podstawowa', 'Rozszerzona', 'Premium', 'Smaki tygodnia']


class Product(models.Model):
    TAG_CHOICES = [
        ('basic', 'Podstawowa'),
        ('extend', 'Rozszerzona'),
        ('premium', 'Premium'),
        ('weekly_flavors', 'Smaki tygodnia'),
    ]

    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', null=True, blank=True,
                              default='products/images/PolishLodyLogo.jpg')
    is_active = models.BooleanField(default=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='basic')

    def __str__(self):
        return self.title

