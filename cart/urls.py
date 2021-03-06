from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<food_id>\d+)/$',views.cart_add,name='add'),
    url(r'^remove/(?P<food_id>\d+)/$',views.cart_remove,name='remove'),
    url(r'^checkout/',views.checkout,name='checkout'), 
]