# Generated by Django 2.2.5 on 2021-04-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catname', models.CharField(max_length=50)),
                ('catid', models.IntegerField()),
            ],
        ),
    ]
