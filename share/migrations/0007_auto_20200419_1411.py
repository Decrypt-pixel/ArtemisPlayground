# Generated by Django 3.0.3 on 2020-04-19 14:11

from django.db import migrations, models
import share.models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(upload_to=share.models.user_directory_path),
        ),
    ]
