from rest_framework import generics
from trading_network.serializers import *
from .models import *


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanyDetailSerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    print(Company.objects.all())


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
