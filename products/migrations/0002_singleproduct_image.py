# Generated by Django 4.1.5 on 2023-03-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleproduct',
            name='image',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='Image'),
        ),
    ]
