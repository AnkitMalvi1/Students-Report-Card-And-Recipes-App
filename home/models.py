from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True,blank=True)
    file = models.FileField(null=True,blank=True)

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)    

    def __str__(self) -> str:
        return self.car_name