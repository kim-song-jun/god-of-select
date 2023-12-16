from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Content


@api_view(['GET'])
def test(request):
    print(request.data)
    return Response({"message": "Content, world!"})


@api_view(['POST'])
def create_content(request):
    print(request.data)

    title = request.data['title']

    content = Content.objects.create(title=title)
    content.save()

    result = {
        "content_id": str(content.content_id),
    }
    
    return Response({"content": result})


@api_view(['POST'])
def search_content(request):
    print(request.data)

    content_id = request.data['content_id']

    content = Content.objects.get(content_id=content_id)

    result = {
        "title": content.title,
        "vote_count": content.vote_count,
    }

    return Response({"content": result})