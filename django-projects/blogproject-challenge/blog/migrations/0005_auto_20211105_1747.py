# Generated by Django 3.2.8 on 2021-11-05 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211105_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]