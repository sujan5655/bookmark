from django.db import models


class Todolist(models.Model): 
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField()