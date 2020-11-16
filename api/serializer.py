from rest_framework import serializers
from .models import *


class VitrinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VitrinCategory
        fields = ('name', )

class VitrinSerializer1(serializers.ModelSerializer):
    category = VitrinCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    class Meta:
        model = Vitrin
        fields = ('id', 'name', 'price', 'discount', 'category', 'image', )

class VitrinSerializer(serializers.ModelSerializer):
    category = VitrinCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    similar1 = VitrinSerializer1()
    similar2 = VitrinSerializer1()
    similar3 = VitrinSerializer1()
    similar4 = VitrinSerializer1()
    class Meta:
        model = Vitrin
        fields = ('id', 'name', 'price', 'discount', 'category', 'ingredient', 'weight', 'image', 'similar1', 'similar2', 'similar3', 'similar4', )

class MarsipanCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarsipanCategory
        fields = ('name', )

class MarsipanSerializer1(serializers.ModelSerializer):
    category = MarsipanCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    class Meta:
        model = Marsipan
        fields = ('id', 'name', 'price', 'discount', 'category', 'image', )

class MarsipanSerializer(serializers.ModelSerializer):
    category = MarsipanCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    similar1 = MarsipanSerializer1()
    similar2 = MarsipanSerializer1()
    similar3 = MarsipanSerializer1()
    similar4 = MarsipanSerializer1()
    class Meta:
        model = Marsipan
        fields = ('id', 'name', 'price', 'discount', 'category', 'ingredient', 'weight', 'image', 'similar1', 'similar2', 'similar3', 'similar4', )

class FlowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerCategory
        fields = ('name', )

class FlowerSerializer1(serializers.ModelSerializer):
    category = FlowerCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    class Meta:
        model = Flower
        fields = ('id', 'name', 'price', 'discount', 'category', 'image', )

class FlowerSerializer(serializers.ModelSerializer):
    category = FlowerCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    similar1 = FlowerSerializer1()
    similar2 = FlowerSerializer1()
    similar3 = FlowerSerializer1()
    similar4 = FlowerSerializer1()
    class Meta:
        model = Flower
        fields = ('id', 'name', 'price', 'discount', 'category', 'ingredient', 'weight', 'image', 'similar1', 'similar2', 'similar3', 'similar4', )

class XoncaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = XoncaCategory
        fields = ('name', )

class XoncaSerializer1(serializers.ModelSerializer):
    category = XoncaCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    class Meta:
        model = Xonca
        fields = ('id', 'name', 'price', 'discount', 'category', 'image', )

class XoncaSerializer(serializers.ModelSerializer):
    category = XoncaCategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    similar1 = XoncaSerializer1()
    similar2 = XoncaSerializer1()
    similar3 = XoncaSerializer1()
    similar4 = XoncaSerializer1()
    class Meta:
        model = Xonca
        fields = ('id', 'name', 'price', 'discount', 'category', 'ingredient', 'weight', 'image', 'similar1', 'similar2', 'similar3', 'similar4', )

class CafeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False) 
    class Meta:
        model = Cafe
        fields = ('id', 'image', )

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class HomePageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageProduct
        fields = '__all__'