# Generated by Django 3.0.4 on 2020-04-26 05:02

from django.db import migrations, models
import share.models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ImageField(default='default.png', upload_to=share.models.user_directory_path),
        ),
    ]
