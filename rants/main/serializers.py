from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Rant, Category

from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        depth = 2


class RantSerializer(WritableNestedModelSerializer):
    categories = CategorySerializer(many=True)
    slug = serializers.SlugField(read_only=True)


    class Meta:
        model = Rant
        fields = ('id', 'title', 'slug', 'categories')
        many = True
        depth=3
