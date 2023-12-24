from django.urls import path
from .views import CartItemListView, CartItemDetailView


urlpatterns = [
    path('cart/', CartItemListView.as_view(), name='cart-list'),
    path('cart/<int:pk>', CartItemDetailView.as_view(), name='cart-detail')

]