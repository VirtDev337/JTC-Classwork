# Generated by Django 3.2.8 on 2021-11-26 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_slug',
        ),
    ]
