from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(Bookmark)
admin.site.register(Todolist)