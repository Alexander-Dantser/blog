# Generated by Django 5.1.4 on 2024-12-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_autor_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
    ]