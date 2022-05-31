# Generated by Django 4.0.3 on 2022-05-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='best_time_easy',
            field=models.DurationField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='best_time_hard',
            field=models.DurationField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='best_time_medium',
            field=models.DurationField(default='00:00:00'),
        ),
    ]
