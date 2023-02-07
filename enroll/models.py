from django.db import models

# Create your models here.
class Signup(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=100)
