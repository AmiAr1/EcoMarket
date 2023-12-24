from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer
# Create your views here.


class CartItemListView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemDetailView(generics.RetrieveAPIView):
    queryset = CartItem.objects.prefetch_related('product').all()
    serializer_class = CartItemSerializer
    lookup_field = 'pk'