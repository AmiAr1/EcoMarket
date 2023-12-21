from django.urls import path
from .views import (CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
                    ProductsListCreateView, ProductsRetrieveUpdateDestroyView,
                    CartItemListView, CartItemDetailView)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('products/', ProductsListCreateView.as_view(), name='products-list-create'),
    path('products/<int:pk>/', ProductsRetrieveUpdateDestroyView.as_view(), name='products-retrieve-update-destroy'),
path('cart/', CartItemListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-detail'),



]
