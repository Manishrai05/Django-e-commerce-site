# Generated by Django 3.1.2 on 2020-12-11 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201211_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pass1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pass2',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
