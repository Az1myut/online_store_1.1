# Generated by Django 4.1.5 on 2023-05-03 02:41

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_brands_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='image_thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='thumbs/%Y/%m/%d'),
        ),
    ]
