from django.db import models
from django.db import models
class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    number=models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=30, null=True)
    address=models.CharField(max_length=100, null=False)
class Garbage(models.Model):
    garbage_type=models.CharField(max_length=50)
    cost_per_unit=models.CharField(max_length=50)
    garbage_quantity=models.CharField(max_length=50)
class Manager(models.Model):
    name=models.CharField(max_length=50, null=False)
    phone=models.CharField(max_length=20,null=False)
    emial = models.CharField(max_length = 50)
    address = models.CharField(max_length = 150)
class DumpArea(models.Model):
    name = models.CharField(max_length=50,null=False)
    address = models.CharField(max_length = 150, null=False)
    destination =models.CharField(max_length=50,  null=False)
    dimension =models.CharField(max_length=20, null=True)
class Place(models.Model):
    name=models.CharField(max_length=50,null=False)
    address=models.CharField(max_length=50,null=False)
    #garbage_id
    #user_id
    #dumparea_id
class Vehicle(models.Model):
    name=models.CharField(max_length = 150)
    number = models.CharField(max_length = 150)
    size=models.CharField(max_length=20, null=True)
    color = models.CharField(max_length = 10)
    brand = models.CharField(max_length = 150)
    model_no=models.CharField(max_length=50)
    # manager_id
class Request(models.Model):
    #user_id
    #manager_id
    #vehicle_id
    time_of_arrival=models.DateTimeField(auto_now_add=True)

    
    
    
    


    

# Create your models here.
