from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
        " Uses HTTP methods as function(get, post, patch ,put, delete)",
        "It is similar to a traditipna django view ",
        "gives yo most control over logic",
        "is mapped manually to urls"
        ]

        return Response({'message': "hello!", 'an_apiview':an_apiview})
    def post(self, request):
        """create a hello message with pur name"""

        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = 'Hello  {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk=None):
        """Handles updating an object"""


        return Response({'method': 'put'})
    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})


    def delete(self, request, pk=None):
        """deletes an ob  ject"""

        return Response({'method': 'delete'})
class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    serializer_class= serializers.HelloSerializer

    def list(self, request):

        """return a hello message"""
        a_viewset= [
            'Uses actions(lsit, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'provides more funcationality wth less code'
        ]

        return Response({'message':'Hello!' , 'a_viewset': a_viewset})


    def create(Self,request):
        """create  anew hello messsage"""
