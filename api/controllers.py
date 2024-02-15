from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloWorldSerializer

# Create your views here.
class HelloWorld(APIView):
    def get(self, request, format=None):
        # serializer = HelloWorldSerializer()
        # return Response(serializer.data)
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        return Response()
    
    

    def post(self, request, format=None):
        
        # serializer = HelloWorldSerializer()
        # return Response(serializer.data)
        data=request.data
        data["Company"] = "Hashmove"
        '''
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }'''
        return Response(data)