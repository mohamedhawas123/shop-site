# Generated by Django 3.1.5 on 2021-01-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210121_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/products/%Y/%m/%d'),
        ),
    ]
