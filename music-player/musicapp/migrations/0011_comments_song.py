# Generated by Django 4.0.5 on 2022-07-06 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0010_rename_artist_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='song',
            field=models.ForeignKey(default='song', on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
    ]