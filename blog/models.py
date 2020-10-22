from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:cat_slug', args=[self.slug, ])


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(default='')

    blog_image = models.ImageField(upload_to='blognew/image', default='')
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:bloghome')

