# Generated by Django 4.2.2 on 2023-07-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_counted_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
    ]
