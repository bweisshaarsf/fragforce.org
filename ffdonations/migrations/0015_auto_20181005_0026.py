# Generated by Django 2.1.2 on 2018-10-05 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ffdonations', '0014_auto_20181005_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationmodel',
            name='id',
            field=models.CharField(editable=False, max_length=1024, primary_key=True, serialize=False,
                                   verbose_name='Donation ID'),
        ),
    ]
