# Generated by Django 2.2 on 2019-07-10 03:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='SubmittedOnDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
