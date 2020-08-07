# Generated by Django 3.0.8 on 2020-08-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='second_images',
        ),
        migrations.AddField(
            model_name='blog',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='main_photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
