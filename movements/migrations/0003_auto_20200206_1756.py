# Generated by Django 3.0.3 on 2020-02-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movements', '0002_auto_20200206_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movement',
            name='lng',
            field=models.FloatField(),
        ),
    ]
