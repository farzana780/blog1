from rest_framework.serializers import ModelSerializer
from blog.models import BlogPost

class Postserializers(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title', 'slug', 'time',
        ]

class PostDetailserializers(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title','slug', 'body', 'blog_image', 'time',
        ]


class PostCreateserializers(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title', 'body', 'slug', 'blog_image', 'time',
        ]
