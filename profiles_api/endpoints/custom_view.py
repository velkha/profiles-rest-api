from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#import custom_serializer
from profiles_api.serializers import custom_serializer

class CustomView(APIView):
    serializer_class = custom_serializer.CustomSerializer
    
    def get(self, request, format=None):
        return Response({'message': 'Hello, World!', 'an_apiview': 'This is a custom view'})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': f'Hello, {name}!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
