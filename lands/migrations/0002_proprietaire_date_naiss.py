# Generated by Django 2.2.2 on 2019-08-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proprietaire',
            name='date_naiss',
            field=models.DateField(default=None),
        ),
    ]