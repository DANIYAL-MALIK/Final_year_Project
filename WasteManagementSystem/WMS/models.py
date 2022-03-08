from django.utils.timezone import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.db import models
from users.models import User

ZONE_CHOICES = [
    ('Ravi Zone', 'Ravi Zone'),
    ('Data Ganj Bukhsh Zone', 'Data Ganj Bukhsh Zone'),
    ("Shalamar Zone", 'Shalamar Zone'),
    ('Aziz Bhatti Zone', 'Aziz Bhatti Zone'),
    ('Samanabad Zone', 'Samanabad Zone'),
    ('Gulberg Zone', 'Gulberg Zone'),
    ('Wahga Zone', 'Wahga Zone'),
    ('Allama Iqbal Zone', 'Allama Iqbal Zone'),
    ('Nishtar Zone', 'Nishtar Zone'),

]

STATUS_CHOICES = [
    ('PENDING', 'PENDING'),
    ('PROCESSING', 'PROCESSING'),
    ('RESOLVED', 'RESOLVED')
]
Vehicle_CHOICES = [
    ('Free', 'Free'),
    ('On_Duty', 'On_duty'),

]

class Garbage(models.Model):
    garbage_type = models.CharField(max_length=50)
    cost_per_unit = models.CharField(max_length=50)
    garbage_quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.garbage_type


class Manager(models.Model):
    zone = models.CharField(choices=ZONE_CHOICES, max_length=50, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.user.username


class DumpArea(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=150, null=False)
    destination = models.CharField(max_length=50, null=False)
    dimension = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    garbage_id = models.ForeignKey(Garbage, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dumparea_id = models.ForeignKey(DumpArea, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    size = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=10)
    brand = models.CharField(max_length=150)
    status=models.CharField(choices=Vehicle_CHOICES,max_length=20,default="Free")
    model_no = models.CharField(max_length=50)
    zone = models.CharField(choices=ZONE_CHOICES, max_length=50, blank=False, null=False,default="Ravi Zone")
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        return reverse("managerPanel")

    def __str__(self):
        return self.name


class Request(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=15, blank=False, default=" ")
    address = models.CharField(max_length=400, null=False)
    zone = models.CharField(choices=ZONE_CHOICES, max_length=50, blank=False, null=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, blank=False, null=False, default='PENDING')
    complaint = models.TextField(blank=False, null=False)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    date_posted = models.DateTimeField(default=datetime.now, null=False)

    def __str__(self):
        return self.zone + ' - ' + self.author.username

    def get_absolute_url(self):
        return reverse("request_detail", args=[str(self.id)])

class Contact(models.Model):
    name=models.CharField(max_length=20, blank=False)
    email=models.EmailField(max_length=30, blank=False)
    zone = models.CharField(choices=ZONE_CHOICES, max_length=50, blank=False, null=False, default="Lahore")
    message=models.TextField(max_length=300,blank=False)
    date_posted = models.DateTimeField(default=datetime.now, null=False)
    def __str__(self):
        return self.email
    def get_absolute_url(self):
        return reverse("home")
