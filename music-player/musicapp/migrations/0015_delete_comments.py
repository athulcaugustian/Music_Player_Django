# Generated by Django 4.0.5 on 2022-07-06 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0014_comments_song'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
