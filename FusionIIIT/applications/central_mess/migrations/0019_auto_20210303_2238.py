# Generated by Django 3.1.5 on 2021-03-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0018_merge_20210303_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_bill',
            name='month',
            field=models.CharField(default=3, max_length=20),
        ),
        migrations.AlterField(
            model_name='monthly_bill',
            name='year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='payments',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]
