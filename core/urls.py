
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index,name = "home"),
    path('createTodo',createTodo),
    path('updateTodo/<int:id>/',updateTodo),
    path('deleteTodo/<int:id>/',deleteTodo),
    path('loginuser',loginuser,name = "loginuser"),
    path("bookmark/Todo/<int:id>",saveBookMark)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

