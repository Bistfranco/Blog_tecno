# Generated by Django 4.2.2 on 2023-07-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, default='../static/post_default.png', null=True, upload_to='blog/articulos/imagenes', verbose_name='Imagen'),
        ),
    ]
