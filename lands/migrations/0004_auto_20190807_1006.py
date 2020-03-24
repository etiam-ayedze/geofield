# Generated by Django 2.2.4 on 2019-08-07 10:06

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0003_auto_20190806_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typesuccession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libTypeSuccession', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='telephone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]