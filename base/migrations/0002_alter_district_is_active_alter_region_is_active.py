# Generated by Django 4.1.10 on 2023-09-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
