from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status

from rest_framework.views import APIView

# Create your views here.

class TestClass(APIView):

    def get(self, request):
        return Response({
            "message": "Hello, world!",
            "status": "API working"
        }, status=status.HTTP_200_OK)
    
# def apiTest(request):
#     if request.method == "GET":
#         return Response({
#             "message": "Hello, world!",
#             "status": "API working"
#         }, status=status.HTTP_200_OK)
#         # return JsonResponse({"message": "Hello, world!", "status": "API working"}, status=status.HTTP_200_OK)
#     else:
#         return Response({
#             "message": "Hello, world!",
#             "status": "API working"
#         }, status=status.HTTP_400_BAD_REQUEST)