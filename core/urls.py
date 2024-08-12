
from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name = "home"),
    path('createTodo',createTodo),
    path('updateTodo/<int:id>/',updateTodo)
]
