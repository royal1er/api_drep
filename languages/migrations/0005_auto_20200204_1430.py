# Generated by Django 3.0 on 2020-02-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0004_auto_20200204_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='Question',
            field=models.CharField(max_length=100),
        ),
    ]
