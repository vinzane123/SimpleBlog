from rest_framework import serializers
from .models import Author, Blog, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fileds = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fileds = '__all__'


class CoomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
