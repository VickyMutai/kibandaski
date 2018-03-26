from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from food.models import Food
from .cart import cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, food_id):
    Cart = cart(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        Cart.add(food=food,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        Cart.save()
    return redirect('cart:cart_detail')

def cart_remove(request, food_id):
    Cart = cart(request)
    food = get_object_or_404(Food, id=food_id)
    Cart.remove(food)
    return redirect('cart:cart_detail')

def cart_detail(request):
    Cart = cart(request)
    foodie = Food.get_food()
    for food in foodie:
        fd = str(food.id)
        print(fd)
    return render(request, 'cart/detail.html',{'foodie':foodie,
                                               'cart':Cart,
                                               'fd':fd,})