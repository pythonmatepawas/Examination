# Generated by Django 2.2.3 on 2020-02-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_no',
            field=models.CharField(max_length=13),
        ),
    ]