# Generated by Django 4.2.2 on 2023-07-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_counted_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
    ]
