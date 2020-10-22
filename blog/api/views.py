from blog.models import BlogPost
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import Postserializers, PostDetailserializers, PostCreateserializers
    # , PostUpdateserializers, PostDeleteserializers

class PostListApiView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = Postserializers

class PostDetailApiView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailserializers
    lookup_field = 'slug'



class PostCreateApiView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostCreateserializers


class PostUpdateApiView(UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailserializers
    lookup_field = 'slug'


class PostDeleteApiView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostDetailserializers
    lookup_field = 'slug'