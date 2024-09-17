import uuid  # tambahkan baris ini di paling atas
from django.db import models

class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    flower = models.CharField(max_length=255) 
    quantity = models.IntegerField()  