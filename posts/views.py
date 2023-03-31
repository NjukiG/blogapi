from django.shortcuts import render

from django.contrib.auth import get_user_model  # new
# from rest_framework import generics

from rest_framework import viewsets # new
from rest_framework.permissions import IsAdminUser  # new

from .models import Post
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import PostSerializer, UserSerializer  # new


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# We switched from generics toviewsets inorder to stop using the code below and instead use the 
# one above which uses ModelViewSet, which includes both  ListView and DetailsView
# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# Create your views here.

# permission_classes = (permissions.IsAdminUser,) # new

