from django.db import models
# from django.contrib.auth.models import AbstractUser
# import datetime
# from django.utils import timezone
import uuid

class Meme(models.Model):
    meme_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)

    content_1 = models.ForeignKey('content.Content', on_delete=models.CASCADE, related_name='meme_content_1')
    content_2 = models.ForeignKey('content.Content', on_delete=models.CASCADE, related_name='meme_content_2')

    primary = models.ForeignKey('meme.MemeDetail', on_delete=models.CASCADE, related_name='primary')
    secondary = models.ForeignKey('meme.MemeDetail', on_delete=models.CASCADE, related_name='secondary')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.meme_id)
    


class MemeDetail(models.Model):
    meme_detail_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    content = models.ForeignKey('content.Content', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.meme_detail_id)

