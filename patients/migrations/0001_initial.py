# Generated by Django 3.0.3 on 2020-02-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=30)),
                ('contact_count', models.IntegerField()),
                ('second_infection', models.IntegerField()),
            ],
        ),
    ]
