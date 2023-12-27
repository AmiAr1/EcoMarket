from django.urls import path
from .views import (CategoryListView, CategoryDetailView,
                    ProductsListView, ProductsDetailView,
                    CartItemListViews)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list-create'),
    path('categories/<int:category_id>/products/', ProductsListView.as_view(), name='products=list'),
    path('products/<int:id>/', ProductsDetailView.as_view(), name='products-detail'),
    path('cart/', CartItemListViews.as_view(), name='cart-list'),
    path('cart-items/<int:id>', CartItemListViews.as_view()),
    # path('cart/<int:pk>', CartItemDetailView.as_view(), name='cart-detail')



    # path('products/', ProductsListCreateView.as_view(), name='products-list-create'),
    # path('cart/', CartItemListView.as_view(), name='cart-list'),
    # path('cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-detail'),



]
