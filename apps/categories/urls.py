from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView, ProductListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('product/', ProductListCreateView.as_view())


]
