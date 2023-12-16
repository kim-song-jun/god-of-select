from django.contrib import admin

# Register your models here.
from .models import Meme, MemeDetail

admin.site.register(Meme)
admin.site.register(MemeDetail)