from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from blog.models import Blog

class BlogSerializer(serializers.Serializer):
    user = CustomUserSerializer(required=False)
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(default="")
    date = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)