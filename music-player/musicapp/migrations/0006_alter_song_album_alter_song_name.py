# Generated by Django 4.0.5 on 2022-06-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_auto_20200712_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
