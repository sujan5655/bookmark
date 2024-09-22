from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import *
from .Serializers import TodolistSerializer
from rest_framework.response import Response


@api_view(['GET'])
def index(request): 
    todolists = Todolist.objects.all()
    serializers = TodolistSerializer(todolists,many = True)
    
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def createTodo(request): 
    
    if request.method == "POST":
        serializers = TodolistSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'success':'data saved successfully'})
        return Response({'error':"data not saved"})
    
@api_view(['PUT','GET'])
def updateTodo(request,id): 
    todo = Todolist.objects.get(id =id)
    if request.method =="PUT": 
        
        serializers = TodolistSerializer(todo,data = request.data)
        if serializers.is_valid(): 
            serializers.save()
            return Response({'data':"data updated successfully",'data':serializers.data})
        return Response({'error':"data not updated"})
    
    serializers = TodolistSerializer(todo)
    
    return Response(serializers.data)

@api_view(['delete'])
def deleteTodo(request,id):
    todo=Todolist.objects.get(id=id)
    todo.delete()
    return Response({'data':"data deleted successfully"})       



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def saveBookMark(request,id):
    # try : 
        todo = Todolist.objects.filter(id = id).first()
        print(todo)
        bookmark = Bookmark.objects.filter(user = request.user,Todo = todo ).first()
        if bookmark: 
            bookmark.delete()
            return Response({'success':True,"message":"bookmarked removed"})
        else: 
            Bookmark.objects.create(user = request.user,Todo = todo)
            return Response({'success':True,"message":"bookmarked saved"})




    # except: 
    #    return Response({'success':False,"message":"Todo not found "})

from rest_framework.authtoken.models import Token


@api_view(["POST"])
def loginuser(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(request.POST)
    user = User.objects.filter(username = username).first()
    print(user)
    if user: 
         if user.check_password(password):
            token = Token.objects.get_or_create(user = user)
            return Response({ "success": True, 'Token':token[0].key})
         else: 
            return Response({ "success": False, 'error':"incorrect password"})        
    else: 
        return Response({ "success": False,  'error':"user not found"})

        