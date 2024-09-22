from django.db import models
from django.contrib.auth.models import User

class Todolist(models.Model): 
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=250,default=False)
    image = models.ImageField(upload_to='img',null=True,blank=True)
    is_completed = models.BooleanField()

class Bookmark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Todo=models.ForeignKey(Todolist,on_delete=models.CASCADE)