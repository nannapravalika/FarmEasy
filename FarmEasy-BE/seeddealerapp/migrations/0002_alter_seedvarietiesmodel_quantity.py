# Generated by Django 4.0.1 on 2022-03-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seeddealerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seedvarietiesmodel',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]
