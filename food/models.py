from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    image_url = models.ImageField(upload_to='food/')
    available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save_food(self):
        self.save()
    
    def delete_food(self):
        self.delete()

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