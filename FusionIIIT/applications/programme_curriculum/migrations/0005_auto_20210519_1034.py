# Generated by Django 3.1.5 on 2021-05-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme_curriculum', '0004_auto_20210509_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='name',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Phd', 'Phd')], max_length=50),
        ),
        migrations.AlterField(
            model_name='courseslot',
            name='type',
            field=models.CharField(choices=[('Professional Core', 'Professional Core'), ('Professional Elective', 'Professional Elective'), ('Professional Lab', 'Professional Lab'), ('Engineering Science', 'Engineering Science'), ('Natural Science', 'Natural Science'), ('Humanities', 'Humanities'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('Management Science', 'Management Science'), ('Optional Elective', 'Optional Elective'), ('Project', 'Project'), ('Optional', 'Optional'), ('Others', 'Others')], max_length=70),
        ),
    ]
