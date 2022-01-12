# Generated by Django 3.2.8 on 2021-11-29 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211128_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
