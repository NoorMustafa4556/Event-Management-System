# Generated by Django 5.2.1 on 2025-05-31 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_date_event_date_time_event_image_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='participant',
            name='achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
    ]
