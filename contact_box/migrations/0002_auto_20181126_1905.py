# Generated by Django 2.1.3 on 2018-11-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_box', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.SmallIntegerField(),
        ),
    ]
