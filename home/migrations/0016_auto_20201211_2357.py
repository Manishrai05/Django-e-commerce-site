# Generated by Django 3.1.2 on 2020-12-11 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20201211_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static\\productImages'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='productDesc',
            field=models.TextField(max_length=300),
        ),
    ]
