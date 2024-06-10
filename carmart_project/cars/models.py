from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.FloatField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
    
class Order(models.Model):     
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order by {self.user.username} for {self.car.name}"

class Comment(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"