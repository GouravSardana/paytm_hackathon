# Generated by Django 2.1.5 on 2019-01-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190112_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_detail',
            name='adhar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_detail',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]