from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>/', views.cart_change, name='cart_change'),
    path('cart_dicrement/<slug:product_slug>/', views.cart_dicrement, name='cart_dicrement'),
    path('cart_remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
]
