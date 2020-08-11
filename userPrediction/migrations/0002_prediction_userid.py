# Generated by Django 2.2.15 on 2020-08-09 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('userPrediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile'),
        ),
    ]
