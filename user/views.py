from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from user_ddk.models import UserDDK

@api_view(['GET'])
def test(request):
    print(request.data)
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def create_user(request, user_name):
    user_name = str(user_name)

    user = User.objects.create(user_name=user_name)
    user.save()

    user_ddk = UserDDK.objects.create(user_id=user)
    user_ddk.save()

    result = {
        "user_id": str(user.user_id),
        "user_name": user.user_name,
    }
    
    return Response({"user": result})


@api_view(['GET'])
def test_create_user(reqeust, user_name):
    
    user_name = str(user_name)

    user = User.objects.create(user_name=user_name)
    user.save()

    user_ddk = UserDDK.objects.create(user_id=user)
    user_ddk.save()

    result = {
        "user_id": str(user.user_id),
        "user_name": user.user_name,
    }

    return Response({"user": result})