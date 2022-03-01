from django.utils.timezone import datetime
from django.db import models
from django.db import models
from django.contrib.auth.models import User
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
    garbage_id=models.ForeignKey(Garbage,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dumparea_id=models.ForeignKey(DumpArea,on_delete=models.CASCADE,null=True)
class Vehicle(models.Model):
    name=models.CharField(max_length = 150)
    number = models.CharField(max_length = 150)
    size=models.CharField(max_length=20, null=True)
    color = models.CharField(max_length = 10)
    brand = models.CharField(max_length = 150)
    model_no=models.CharField(max_length=50)
    manager_id=models.ForeignKey(Manager,on_delete=models.CASCADE,null=True)
class Request(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20,null=False,default="user")
    email=models.EmailField(max_length=40,null=True)
    phone=models.CharField(max_length=15,blank=False,default=" ")
    address=models.CharField(max_length=400,null=False)
    zone=models.CharField(max_length=20, blank=True, null=True)
    complaint=models.CharField(max_length=400, blank=True, null=True)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    date_posted=models.DateTimeField(default=datetime.now,null=False)


    
    
    
    


    

# Create your models here.
