# Generated by Django 3.2 on 2021-04-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccsformdata',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
