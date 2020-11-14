from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )

class CakeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    image = serializers.ImageField(use_url=False)
    class Meta:
        model = Cake
        fields = ('id', 'name', 'price', 'discount', 'category', 'ingredient', 'weight', 'image', 'similar1', 'similar2', 'similar3', 'similar4', )

class MarsipanCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarsipanCategory
        fields = ('name', )

class MarsipanSerializer(serializers.ModelSerializer):
    category = MarsipanCategorySerializer(read_only=True)
    class Meta:
        model = Marsipan
        fields = '__all__'

class FlowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerCategory
        fields = ('name', )

class FlowerSerializer(serializers.ModelSerializer):
    category = FlowerCategorySerializer(read_only=True)
    class Meta:
        model = Flower
        fields = '__all__'

class XoncaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = XoncaCategory
        fields = ('name', )

class XoncaSerializer(serializers.ModelSerializer):
    category = XoncaCategorySerializer(read_only=True)
    class Meta:
        model = Xonca
        fields = '__all__'

class CafeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False) 
    class Meta:
        model = Cafe
        fields = ('id', 'image', )

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'