from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='pics')
    description= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)

def _str_(self):
    return self.name