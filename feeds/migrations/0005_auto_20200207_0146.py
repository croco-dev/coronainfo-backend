# Generated by Django 3.0.3 on 2020-02-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20200207_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='contact_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
