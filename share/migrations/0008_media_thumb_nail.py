# Generated by Django 3.0.4 on 2020-04-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='thumb_nail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]