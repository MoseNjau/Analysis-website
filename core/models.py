from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.EmailField(max_length=255)
    full_name =models.CharField(max_length=100)
    subject =models.CharField(max_length=100)
    message =models.TextField()
