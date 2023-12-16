from django.db import models
# from django.contrib.auth.models import AbstractUser
# import datetime
# from django.utils import timezone
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        ordering = ['-created_at']
