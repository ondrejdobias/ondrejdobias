from django.contrib import admin

# Register your models here.
from .models import datainsert
from .models import post

admin.site.register(datainsert)
admin.site.register(post)
