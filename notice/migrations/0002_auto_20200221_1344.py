# Generated by Django 3.0.3 on 2020-02-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
