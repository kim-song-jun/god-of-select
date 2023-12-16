from django.db import models
# from django.contrib.auth.models import AbstractUser
# import datetime
# from django.utils import timezone
import uuid

class Issue(models.Model):
    issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content_1 = models.ForeignKey('content.Content', on_delete=models.CASCADE, related_name='issue_content_1')
    content_2 = models.ForeignKey('content.Content', on_delete=models.CASCADE, related_name='issue_content_2')
    all_vote_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.issue_id)
