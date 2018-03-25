from decimal import Decimal
from django.conf import settings
from food.models import Food

class Cart(object):
    def __init__(self,request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    def add(self,Food,quantity=1,update_quantity=False):
        """
        Add product to cart or 
        """
        food_id = str(Food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity':0,
                                  'price':str(Food.price)}

        if update_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
        self.save()

    def save(self):
        #update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        #mark the session as modified to make sure it is saved
        self.session.modified = True

    def remove(self, Food):
        """
        Remove a product from the cart.
        """
        food_id = str(Food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()

    def __iter__(self):
        """
        iterate over the items in the cart and get the products from the database
        """
        food_ids = self.cart.keys()
        foods = Food.objects.filter(id__in=food_ids)
        for food in foods:
            self.cart[str(food.id)]['food'] = food

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''
        count all items in the cart
        '''
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        #remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True