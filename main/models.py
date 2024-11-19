import uuid  # tambahkan baris ini di paling atas
from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    flower = models.CharField(max_length=255)  
    quantity = models.IntegerField()  

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

class Employee(models.Model):
    department = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)
    user = models.OneToOneField(User, on_delete=models.CASCADE)