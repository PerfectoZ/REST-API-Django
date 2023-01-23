from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP Methods as function (get, put, post, patch, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'hello', 'an_apiview': an_apiview})
