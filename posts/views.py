from django.contrib.auth import get_user_model # new

from rest_framework import viewsets

from .models import Post

from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser # new

from .serializers import *

class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all() 
    serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView): 
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet): # new 
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all() 
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new 
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
