# Generated by Django 3.1.2 on 2020-10-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201014_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]