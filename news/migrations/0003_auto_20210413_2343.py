# Generated by Django 2.2.5 on 2021-04-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210413_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='act',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='ocatid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='news',
            name='rand',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.TextField(default=''),
        ),
    ]
