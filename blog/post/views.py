from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


# Create your views here.

def post_list(request):
	post_list = Post.objects.filter(published_date__isnull=False)
	return render(request, template_name='post_list.html', context={'posts': post_list})


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [permissions.AllowAny]


class PostList(ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	# permission_classes = [permissions.AllowAny]


class PostDetail(RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	# permission_classes = [permissions.AllowAny]




