# Generated by Django 3.1.2 on 2020-12-11 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_product_productdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.IntegerField(max_length=10),
        ),
    ]
