# Generated by Django 4.2.2 on 2023-07-19 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
