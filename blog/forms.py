from django import forms

from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'category', 'blog_image')

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'author': forms.Select(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        #
        #     'blog_image': forms.FileInput(attrs={'class': 'form-control'}),
        # }



class EditForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','body','category','blog_image')
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        #     'blog_image': forms.FileInput(attrs={'class': 'form-control'}),
        # }
