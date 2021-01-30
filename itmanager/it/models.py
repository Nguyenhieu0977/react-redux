from django.db import models

# Create your models here.
class It(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    message = models.CharField(max_length=5000, blank=True)
    create_at = models.DateField(auto_now_add=True)