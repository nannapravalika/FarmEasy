# Generated by Django 4.0.1 on 2022-03-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machinerydealerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmachinerymodel',
            name='machinery_id',
            field=models.IntegerField(null=True),
        ),
    ]
