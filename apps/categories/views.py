from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Products, CartItem
from .serializers import CategorySerializer, ProductsSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Products.objects.filter(category_id=category_id)


class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CartItemListViews(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(CartItem, id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('product_id')
            quantity = serializer.validated_data.get('quantity')

            try:
                product = Products.objects.get(id=product_id)
            except Products.DoesNotExist:
                return Response({"status": "error", "data": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            cart_item, created = CartItem.objects.get_or_create(product_id=product_id)

            max_quantity = 100  # Замените на нужное вам значение
            if cart_item.quantity + quantity > max_quantity:
                return Response({"status": "error", "data": "Quantity exceeds the limit"},
                                status=status.HTTP_400_BAD_REQUEST)

            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()

            return Response({"status": "success", "data": "Product added to cart"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            if 'quantity' in request.data and request.data['quantity'] < 0:
                return Response({"status": "error", "data": "Quantity cannot be negative"},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

# class CartItemListView(generics.ListCreateAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer


# class CartItemDetailView(generics.RetrieveAPIView):
#     queryset = CartItem.objects.prefetch_related('product').all()
#     serializer_class = CartItemSerializer
#     lookup_field = 'pk'
# class CartItemListView(generics.ListCreateAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#
#
# class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
