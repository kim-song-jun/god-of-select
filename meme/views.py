from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Meme, MemeDetail


@api_view(['GET'])
def test(request):
    print(request.data)
    return Response({"message": "Meme, world!"})

