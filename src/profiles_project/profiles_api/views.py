from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_apiview = [
        " Uses HTTP methods as function(get, post, patch ,put, delete)",
        "It is similar to a traditipna django view ",
        "gives yo most control over logic",
        "is mapped manually to urls"
        ]

        return Response({'message': "hello!", 'an_apiview':an_apiview})
