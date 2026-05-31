from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from blog.models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField(source='blog.id', read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "comment", "created_at"]

class BlogListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='date', read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]

class BlogDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='date', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at", "comments"]