from rest_framework.views import APIView
from rest_framework.response import Response

class CustomView(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello, World!', 'an_apiview': 'This is a custom view'})
    
    def post(self, request):
        return Response({'message': 'This is a POST request'})
    
    def put(self, request):
        return Response({'message': 'This is a PUT request'})
    
    def delete(self, request):
        return Response({'message': 'This is a DELETE request'})
    
    def patch(self, request):
        return Response({'message': 'This is a PATCH request'})
    
    def head(self, request):
        return Response({'message': 'This is a HEAD request'})
    
    def options(self, request):
        return Response({'message': 'This is an OPTIONS request'})
    
    def trace(self, request):
        return Response({'message': 'This is a TRACE request'})
    
    def connect(self, request):
        return Response({'message': 'This is a CONNECT request'})
    
    def copy(self, request):
        return Response({'message': 'This is a COPY request'})
    
    def lock(self, request):
        return Response({'message': 'This is a LOCK request'})
    
