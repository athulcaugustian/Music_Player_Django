# Generated by Django 4.0.5 on 2022-07-06 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0013_remove_comments_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
    ]
