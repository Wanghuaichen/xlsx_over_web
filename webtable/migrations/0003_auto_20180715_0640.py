# Generated by Django 2.0.7 on 2018-07-15 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtable', '0002_auto_20180715_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='Scheduled_downtime_per_shirft',
        ),
        migrations.RemoveField(
            model_name='production',
            name='Unscheduled_downtime_lost_per_shirft',
        ),
    ]
