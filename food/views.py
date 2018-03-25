from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Food,Category

# Create your views here.
def index(request):
    test = 'Working!!'
    current_user = request.user
    food = Food.get_food()
    return render(request,'index.html',{"test":test,
                                        "current_user":current_user,
                                        "food":food})

def food(request,food_id):
    try:
        food = Food.objects.get(id=food_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'food/food.html',{"food":food})
