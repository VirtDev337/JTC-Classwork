# Generated by Django 3.2.8 on 2021-11-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='response',
            field=models.ManyToManyField(to='blog.Comment'),
        ),
    ]
