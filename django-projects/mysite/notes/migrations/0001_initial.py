# Generated by Django 3.2.8 on 2021-10-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
    ]
