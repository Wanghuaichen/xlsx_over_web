# Generated by Django 2.0.7 on 2018-07-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtable', '0003_auto_20180715_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='Net_production_time_per_shift',
            field=models.CharField(max_length=20),
        ),
    ]