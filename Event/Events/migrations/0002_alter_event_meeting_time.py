# Generated by Django 4.2.2 on 2023-06-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='meeting_time',
            field=models.DateTimeField(),
        ),
    ]
