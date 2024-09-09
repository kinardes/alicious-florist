from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    flower = models.CharField(max_length=255) 
    quantity = models.IntegerField()  