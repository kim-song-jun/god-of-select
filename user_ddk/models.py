from django.db import models
# from django.contrib.auth.models import AbstractUser
# import datetime
# from django.utils import timezone
import uuid    

class UserDDK(models.Model):
    user_ddk_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    # issue_id = models.ForeignKey('issue.Issue', on_delete=models.CASCADE)
    issues = models.ManyToManyField('issue.Issue', related_name='user_ddk_issues')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_ddk_id)
    
    class Meta:
        ordering = ['-created_at']
