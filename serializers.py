from rest_framework import serializers
from .models import Blogs, SideBlog, User
from django.contrib.auth import get_user_model

User = get_user_model()  

class BlogsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)  # Auto-set user ID

    class Meta:
        model = Blogs
        fields = '__all__'

class SideBlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)  # Auto-set user ID
    class Meta:
        model = SideBlog
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
