from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    items = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

class users(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username