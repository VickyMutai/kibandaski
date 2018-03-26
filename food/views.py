from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Food,Category
from cart.forms import CartAddProductForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    test = 'Working!!'
    current_user = request.user
    food = Food.get_food()
    return render(request,'index.html',{"test":test,
                                        "current_user":current_user,
                                        "Food":food})

@login_required(login_url='/accounts/login/')
def food(request,food_id):
    try:
        food = Food.objects.get(id=food_id)
        cart_product_form = CartAddProductForm()
    except DoesNotExist:
        raise Http404()
    return render(request,'food/food.html',{"food":food,
                                            "cart_product_form":cart_product_form})
