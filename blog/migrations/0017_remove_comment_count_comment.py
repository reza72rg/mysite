# Generated by Django 4.2.2 on 2023-07-25 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_comment_count_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='count_comment',
        ),
    ]
