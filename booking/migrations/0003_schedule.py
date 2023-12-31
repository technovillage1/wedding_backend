# Generated by Django 4.1.10 on 2023-10-22 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_attachment_options_alter_review_options_and_more'),
        ('booking', '0002_alter_booking_service_alter_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('time', models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], max_length=50)),
                ('date', models.DateField()),
                ('is_booked', models.BooleanField(blank=True, default=False)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.booking')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
