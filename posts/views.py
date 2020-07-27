from django.shortcuts import render
from posts.models import Post ,Comment
from posts.serializer import PostSerializer ,CommentSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status ,permissions ,filters
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from posts.permissions import UpdateOwnPost

# Create your views here.

class Posts_ViewSet(viewsets.ModelViewSet):
    # if define Default django rest permission in settting.py then remove it from here 
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,UpdateOwnPost]
    serializer_class= PostSerializer
    queryset = Post.objects.all()
    filter_backends=(filters.SearchFilter,)
    search_fields=('title','body',)

    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
            # not raise exception because add permissions for adding new posts !!!
        else:
            raise Exception ("Must Login To Post Your Own Articles !!!")
      

class Comment_ViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends=(filters.SearchFilter,)
    search_fields=('comment','status')

    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save(make_comment='Anonymous User')


class UserLoginAPIView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


# when anonymous user make a comment create a anonymous_user for you not efficient (this anonymous_user store in database !!!!!)
# best solution save its comment only 
def create_anonymous_user():
    anonymous=User.objects.create(username='anonymous',password='123')
    return anonymous

