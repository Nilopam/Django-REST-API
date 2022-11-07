from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 10)
    date_of_join = models.DateField(auto_now = False)

    def __str__(self):
        return self.name

class EmpProject(models.Model):
    name = models.ForeignKey(Emp,related_name='projects',on_delete = models.CASCADE)
    project = models.CharField(max_length = 200)
    role = models.CharField(max_length = 200)


