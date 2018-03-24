from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Food,Cart

# Create your views here.
def index(request):
    test = 'Working!!'
    current_user = request.user
    food = Food.get_food()
    return render(request,'index.html',{"test":test,
                                        "current_user":current_user,
                                        "food":Food})
