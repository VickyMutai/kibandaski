from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Food(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save_food(self):
        self.save()
    
    def delete_food(self):
        self.delete()

    @classmethod
    def get_food(cls):
        food = cls.objects.all()
        return food

    @classmethod
    def search_food(cls,search_term):
        food = cls.objects.filter(name__icontains=search_term)
        return food

class Cart(models.Model):
    items = models.CharField(max_length=255)
    prices = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)

    def __str__(self):
        return self.items

    def save_cart(self):
        self.save()

    def delete_cart(self):
        self.delete()