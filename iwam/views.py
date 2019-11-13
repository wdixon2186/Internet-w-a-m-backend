from django.shortcuts import render
from rest_framework import generics
from .serializers import ScriptSerializer, CommentSerializer
from .models import Script, Comment


class ScriptList(generics.ListCreateAPIView):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer


class ScriptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
