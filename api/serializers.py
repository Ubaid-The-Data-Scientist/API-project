from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField(default="Hello, World!")
    

class HelloWorldInputSerializer(serializers.Serializer):
    message = serializers.CharField()