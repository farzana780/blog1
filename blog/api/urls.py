from django.urls import path
from blog.api.views import PostListApiView, PostDetailApiView, PostUpdateApiView, PostDeleteApiView, PostCreateApiView



urlpatterns = [

    path('',PostListApiView.as_view(), name='list'),
    path('<slug>',PostDetailApiView.as_view(), name='details'),
    path('create/',PostCreateApiView.as_view(), name='create'),
    path('<slug>/edit/', PostUpdateApiView.as_view(), name='edit_post'),
    path('<slug>/delete', PostDeleteApiView.as_view(), name='post_delete'),


]
