from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Products, CartItem
from .serializers import CategorySerializer, ProductsSerializer, CartItemSerializer


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

# class ProductsListCreateView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer


class CartItemListView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            # Логика добавления товара в корзину
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # Логика получения и отображения корзины
        cartitem = {}  # Замените эту строку на вашу логику получения корзины
        serializer = CartItemSerializer(cartitem.values(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
