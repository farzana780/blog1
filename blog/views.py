from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView

from blog.forms import PostForm, EditForm
from blog.models import BlogPost,Category


def bloghome(request,cat_slug=None):
    cat = None
    post = BlogPost.objects.all()
    category = Category.objects.all()
    if cat_slug:
        cat = get_object_or_404(category, slug= cat_slug)
        post = post.filter(category=cat)

    return render(request, 'blog/bloghome.html', {'post': post, 'category': category, 'cat': cat})



class AddPost(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePost(UpdateView):
    model = BlogPost
    form_class = EditForm
    template_name = "blog/update_post.html"