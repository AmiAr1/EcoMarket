from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView  # ProductsListCreateView, CartItemListView, CartItemDetailView


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/products', CategoryDetailView.as_view(), name='category-detail')
    # path('products/', ProductsListCreateView.as_view(), name='products-list-create'),
    # path('cart/', CartItemListView.as_view(), name='cart-list'),
    # path('cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-detail'),



]
