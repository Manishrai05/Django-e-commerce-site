# Generated by Django 3.1.2 on 2020-12-14 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201215_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productID',
            new_name='id',
        ),
    ]
