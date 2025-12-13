from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return Response({
        "message": "Welcome to the Social Media API!",
        "endpoints": {
            "register": "/api/accounts/register/",
            "login": "/api/accounts/login/",
            "profile": "/api/accounts/profile/"
        }
    })
