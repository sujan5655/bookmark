from rest_framework import serializers
from .models import *
class TodolistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todolist
        fields = "__all__"