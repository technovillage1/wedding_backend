# Generated by Django 4.1.10 on 2023-09-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_attachment_attachment_alter_attachment_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
