# Generated by Django 2.2 on 2019-06-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('City', models.CharField(blank=True, max_length=264)),
                ('Name', models.CharField(max_length=264)),
                ('Gender', models.CharField(blank=True, max_length=264)),
                ('EmailId', models.CharField(blank=True, max_length=264)),
                ('ContactNo', models.CharField(blank=True, max_length=264)),
                ('LocationFrom', models.CharField(blank=True, max_length=264)),
                ('LocationTo', models.CharField(blank=True, max_length=264)),
                ('LoginTime', models.CharField(blank=True, max_length=264)),
                ('LogoutTime', models.CharField(blank=True, max_length=264)),
                ('CompanyName', models.CharField(blank=True, max_length=264)),
                ('TravalToWork', models.CharField(blank=True, max_length=264)),
                ('TravelToWorkOther', models.CharField(blank=True, max_length=264)),
                ('MonthlySpend', models.CharField(blank=True, max_length=264)),
                ('HearAboutUs', models.CharField(blank=True, max_length=264)),
                ('SubmittedOn', models.CharField(blank=True, max_length=264)),
                ('Lead_Status', models.CharField(choices=[('Interested', 'Interested'), ('Undecided', 'Undecided'), ('Uncontacted', 'Uncontacted'), ('Converted', 'Converted')], default='Uncontacted', max_length=264)),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads Collected',
            },
        ),
    ]
