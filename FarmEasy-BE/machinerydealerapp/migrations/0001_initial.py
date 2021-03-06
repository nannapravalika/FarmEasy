# Generated by Django 4.0.1 on 2022-03-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMachineryModel',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('machinery_type', models.CharField(max_length=100)),
                ('specifications', models.TextField()),
                ('function', models.TextField()),
                ('sold_by', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('video', models.FileField(upload_to='videos/')),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'machinery_details',
            },
        ),
        migrations.CreateModel(
            name='MachineryDealerModel',
            fields=[
                ('machinery_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(help_text='Enter First name', max_length=100)),
                ('email', models.EmailField(help_text='Enter email', max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('membership', models.CharField(max_length=100)),
                ('licence_no', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(help_text='Enter Password', max_length=100)),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
            options={
                'db_table': 'machinery_dealer_details',
            },
        ),
    ]
