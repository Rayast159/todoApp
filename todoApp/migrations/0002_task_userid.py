# Generated by Django 3.2 on 2021-04-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='userId',
            field=models.IntegerField(default=-1),
        ),
    ]
