# Generated by Django 2.2.5 on 2021-04-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='main',
            name='tell',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
