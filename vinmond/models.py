from django.db import models

# Create your models here.

class fooditemsss(models.Model):
    id = int 
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    price = models.IntegerField()
    discount = models.BooleanField(default=False)
    desc = models.TextField()
    


























