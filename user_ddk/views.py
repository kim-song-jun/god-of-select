from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDDK


@api_view(['GET'])
def test(request):
    print(request.data)
    return Response({"message": "Hello, world!"})

