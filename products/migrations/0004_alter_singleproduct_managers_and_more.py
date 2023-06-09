# Generated by Django 4.1.5 on 2023-03-16 07:43

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage_remove_singleproduct_image_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='singleproduct',
            managers=[
                ('latest_products', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='singleproduct',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='Категория товара'),
        ),
        migrations.AlterField(
            model_name='singleproduct',
            name='images',
            field=models.ManyToManyField(blank=True, to='products.productimage', verbose_name='Картины'),
        ),
    ]
