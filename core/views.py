from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .Serializers import TodolistSerializer
from rest_framework.response import Response

@api_view(['GET'])
def index(request): 
    todolists = Todolist.objects.all()
    serializers = TodolistSerializer(todolists,many = True)
    
    return Response(serializers.data)



@api_view(['POST'])
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

        

        