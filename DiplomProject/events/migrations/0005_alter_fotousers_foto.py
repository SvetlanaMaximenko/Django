# Generated by Django 4.2.4 on 2023-09-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_fotousers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotousers',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='events/media/'),
        ),
    ]
