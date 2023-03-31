from django.shortcuts import render

from django.contrib.auth import get_user_model  # new
from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import PostSerializer, UserSerializer  # new

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# Create your views here.

# permission_classes = (permissions.IsAdminUser,) # new

