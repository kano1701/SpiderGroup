from rest_framework import serializers
from trading_network.models import *


class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):
    trading_network = serializers.StringRelatedField(many=False)
    district_list = serializers.StringRelatedField(many=True)
    product_list = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'trading_network', 'product_list', 'district_list')


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Company
        fields = ('id', 'name', 'category')