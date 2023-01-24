from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

class Task(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
