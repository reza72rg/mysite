# Generated by Django 4.2.2 on 2023-07-12 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='counted_views',
        ),
    ]