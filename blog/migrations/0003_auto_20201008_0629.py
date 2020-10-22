# Generated by Django 3.1.2 on 2020-10-08 06:29

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201008_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default='', upload_to='blognew/image'),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default='sports', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]