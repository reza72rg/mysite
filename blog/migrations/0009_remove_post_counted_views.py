# Generated by Django 4.2.2 on 2023-07-12 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_counted_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='counted_views',
        ),
    ]