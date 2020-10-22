from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

from blog.views import AddPost,UpdatePost

app_name = 'blog'

urlpatterns = [

    path('', views.bloghome, name='bloghome'),
    path('<slug:cat_slug>', views.bloghome,name='cat_slug'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('edit_post/<int:pk>', UpdatePost.as_view(), name='edit_post'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
