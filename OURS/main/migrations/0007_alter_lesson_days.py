# Generated by Django 3.2.5 on 2021-09-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210903_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='days',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
