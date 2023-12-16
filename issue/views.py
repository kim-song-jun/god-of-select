from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Issue
from user.models import User
from content.models import Content
from user_ddk.models import UserDDK

@api_view(['GET'])
def test(request):
    print(request.data)
    return Response({"message": "Issue, world!"})

@api_view(['GET'])
def test_create(request, user_id):
    user_id = str(user_id)
    title = 'test_get issue'
    content_1 = 'test_get content_1'
    content_2 = 'test_get content_2'

    user = User.objects.get(user_id=user_id)
    content_db_1 = Content.objects.create(title=content_1)
    content_db_2 = Content.objects.create(title=content_2)

    content_db_1.save()
    content_db_2.save()

    issue = Issue.objects.create(
        user_id=user,
        title=title,
        content_1=content_db_1,
        content_2=content_db_2,
    )

    issue.save()

    user_ddk = UserDDK.objects.get(user_id=user)
    user_ddk.issues.add(issue)
    user_ddk.save()

    result = {
        "issue_id": str(issue.issue_id),
    }
    return Response({"issue": result})


@api_view(['GET'])
def test_search(request, user_id):
    user_id = str(user_id)
    issue_id = 'de0bbf18-99ea-4714-983f-a3ad5b4ab6e4'

    issue = Issue.objects.get(issue_id=issue_id)

    user_ddk = UserDDK.objects.get(user_id=user_id)

    user_ddk_issues = user_ddk.issues
    for user_ddk_issue in user_ddk_issues.all():
        if user_ddk_issue.issue_id == issue.issue_id:
            return Response({"error": "user already voted this issue."})

    result = {
        'title': issue.title,
        'id': issue.issue_id,
        'content_1': {
            'id': issue.content_1.content_id,
            'title': issue.content_1.title,
            'vote_count': issue.content_1.vote_count,
        },
        'content_2': {
            'id': issue.content_2.content_id,
            'title': issue.content_2.title,
            'vote_count': issue.content_2.vote_count,
        },
        'all_vote_count': issue.all_vote_count,
    }

    return Response({"issue": result})


@api_view(['GET'])
def test_vote(reqeust, user_id):
    user_id = str(user_id)
    issue_id = 'de0bbf18-99ea-4714-983f-a3ad5b4ab6e4'
    content_id = '6e5d1281-5d9c-44e4-9087-0ee17db54ee5'

    issue = Issue.objects.get(issue_id=issue_id)
    content = Content.objects.get(content_id=content_id)

    user_ddk = UserDDK.objects.get(user_id=user_id)

    user_ddk_issues = user_ddk.issues
    for user_ddk_issue in user_ddk_issues.all():
        if user_ddk_issue.issue_id == issue.issue_id:
            return Response({"error": "user already voted this issue."})

    user_ddk.issues.add(issue)
    user_ddk.save()

    if content.content_id == issue.content_1.content_id or content.content_id == issue.content_2.content_id:
        content.vote_count += 1
        content.save()
        issue.refresh_from_db()
        issue.all_vote_count = issue.content_1.vote_count + issue.content_2.vote_count
        issue.save()

    result = {
        'title': issue.title,
        'id': issue.issue_id,
        'content_1': {
            'id': issue.content_1.content_id,
            'title': issue.content_1.title,
            'vote_count': issue.content_1.vote_count,
        },
        'content_2': {
            'id': issue.content_2.content_id,
            'title': issue.content_2.title,
            'vote_count': issue.content_2.vote_count,
        },
        'all_vote_count': issue.all_vote_count,
    }

    return Response({"issue": result})


@api_view(['POST'])
def create_issue(request):
    print(request.data)

    user_id = request.data.get('user_id', None)
    if user_id is None:
        return Response({"error": "user_id is required."})
    
    user = User.objects.get(user_id=user_id)
    
    if user is None:
        return Response({"error": "user_id is invalid."})
    

    title = request.data.get('title', None)
    content_1 = request.data.get('content_1', None)
    content_2 = request.data.get('content_2', None)

    if title is None or content_1 is None or content_2 is None:
        return Response({"error": "title, content_1, content_2 are required."})
    
    content_db_1 = Content.objects.create(title=content_1)
    content_db_2 = Content.objects.create(title=content_2)
    content_db_1.save()
    content_db_2.save()

    issue = Issue.objects.create(
        user_id=user,
        title=title,
        content_1=content_db_1,
        content_2=content_db_2,
    )
    issue.save()

    user_ddk = UserDDK.objects.get(user_id=user)
    user_ddk.issues.add(issue)
    user_ddk.save()

    result = {
        "issue_id": str(issue.issue_id),
    }
    
    return Response(result)


@api_view(['POST'])
def search_issue(request):
    print(request.data)

    user_id = request.data.get('user_id', None)
    issue_id = request.data.get('issue_id', None)

    if user_id is None and issue_id is None:
        return Response({"error": "user_id or issue_id is required."})
    
    issue = Issue.objects.get(issue_id=issue_id)

    user_ddk = UserDDK.objects.get(user_id=user_id)
    user_ddk_issues = user_ddk.issues

    for user_ddk_issue in user_ddk_issues.all():
        if user_ddk_issue.issue_id == issue.issue_id:
            return Response({"error": "user already voted this issue."})
    
    if issue is None:
        return Response({"error": "issue_id is invalid."})
    
    result = {
        'title': issue.title,
        'id': issue.issue_id,
        'content_1': {
            'id': issue.content_1.content_id,
            'title': issue.content_1.title,
            'vote_count': issue.content_1.vote_count,
        },
        'content_2': {
            'id': issue.content_2.content_id,
            'title': issue.content_2.title,
            'vote_count': issue.content_2.vote_count,
        },
        'all_vote_count': issue.all_vote_count,
    }

    return Response({"issue": result})


@api_view(['POST'])
def vote_issue(request):
    print(request.data)

    user_id = request.data.get('user_id', None)
    issue_id = request.data.get('issue_id', None)
    content_id = request.data.get('content_id', None)


    if user_id is None or issue_id is None or content_id is None:
        return Response({"error": "user_id and issue_id are required."})
    
    issue = Issue.objects.get(issue_id=issue_id)

    if issue is None:
        return Response({"error": "issue_id is invalid."})
    

    user_ddk = UserDDK.objects.get(user_id=user_id)

    user_ddk_issues = user_ddk.issues

    for user_ddk_issue in user_ddk_issues.all():
        if user_ddk_issue.issue_id == issue.issue_id:
            return Response({"error": "user already voted this issue."})

    user_ddk.issues.add(issue)
    user_ddk.save()
    
    content = Content.objects.get(content_id=content_id)

    if content is None:
        return Response({"error": "content_id is invalid."})
    
    if content.content_id == issue.content_1.content_id or content.content_id == issue.content_2.content_id:
        content.vote_count += 1
        content.save()
        issue.refresh_from_db()
        issue.all_vote_count = issue.content_1.vote_count + issue.content_2.vote_count
        issue.save()
    
    result = {
        'title': issue.title,
        'id': issue.issue_id,
        'content_1': {
            'id': issue.content_1.content_id,
            'title': issue.content_1.title,
            'vote_count': issue.content_1.vote_count,
        },
        'content_2': {
            'id': issue.content_2.content_id,
            'title': issue.content_2.title,
            'vote_count': issue.content_2.vote_count,
        },
        'all_vote_count': issue.all_vote_count,
    }


    return Response({"issue": result})


@api_view(['GET', 'POST'])
def search_hot_issue(request):
    if request.method == 'POST':
        user_id = request.data.get('user_id', None)
        user = User.objects.get(user_id=user_id)
        user_ddk = UserDDK.objects.get(user_id=user)
        user_ddk_issues = user_ddk.issues.all()
    issues = Issue.objects.all().order_by('-all_vote_count')

    result = []

    for issue in issues:
        if request.method == 'POST':
            if issue in user_ddk_issues:
                continue
        result.append({
            'title': issue.title,
            'id': issue.issue_id,
            'content_1': {
                'id': issue.content_1.content_id,
                'title': issue.content_1.title,
                'vote_count': issue.content_1.vote_count,
            },
            'content_2': {
                'id': issue.content_2.content_id,
                'title': issue.content_2.title,
                'vote_count': issue.content_2.vote_count,
            },
            'all_vote_count': issue.all_vote_count,
        })
        if len(result) == 10:
            break
    
    return Response({"issues": result})


@api_view(['GET', 'POST'])
def search_all_issue(request):
    if request.method == 'POST':
        user_id = request.data.get('user_id', None)
        user = User.objects.get(user_id=user_id)
        user_ddk = UserDDK.objects.get(user_id=user)
        user_ddk_issues = user_ddk.issues.all()

    issues = Issue.objects.all().order_by('created_at')
    result = []

    for issue in issues:
        if request.method == 'POST':
            if issue in user_ddk_issues:
                continue
        result.append({
            'title': issue.title,
            'id': issue.issue_id,
            'content_1': {
                'id': issue.content_1.content_id,
                'title': issue.content_1.title,
                'vote_count': issue.content_1.vote_count,
            },
            'content_2': {
                'id': issue.content_2.content_id,
                'title': issue.content_2.title,
                'vote_count': issue.content_2.vote_count,
            },
            'all_vote_count': issue.all_vote_count,
        })
        if len(result) == 10:
            break

    return Response({"issues": result})
