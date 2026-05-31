from rest_framework import serializers

class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField(required=False)