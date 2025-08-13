from django.db import models

# Create your models here.
class Team(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    
    
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.age}"