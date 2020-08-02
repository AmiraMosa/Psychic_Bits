# Generated by Django 3.0.8 on 2020-08-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('HT', models.CharField(max_length=20, verbose_name='Home Team')),
                ('AT', models.CharField(max_length=20, verbose_name='Away Team')),
                ('pred', models.CharField(blank=True, max_length=1, verbose_name='Model Prediction')),
                ('FTR', models.CharField(blank=True, max_length=1, verbose_name='Full Time Result')),
            ],
        ),
    ]
