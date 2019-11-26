from django.shortcuts import render
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
# Create your views here.
from .models import *
from .serializers import *



class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-list"

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"


class CategorieList(ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    name = "categorie-list"

class CategorieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    name = "categorie-detail"


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-list"

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-detail"

class PartList(ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    name = "part-list"

class PartDetail(RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    name = "part-detail"

class StepList(ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    name = "step-list"

class StepDetail(RetrieveUpdateDestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    name = "step-detail"    
