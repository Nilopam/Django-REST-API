from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=50)
    joining_date = models.DateField(auto_now=False)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name