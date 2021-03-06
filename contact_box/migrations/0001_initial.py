# Generated by Django 2.1.3 on 2018-11-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('building_number', models.SmallIntegerField()),
                ('flat_number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_box.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.SmallIntegerField(max_length=15)),
                ('type', models.SmallIntegerField(choices=[(1, 'domowy'), (2, 'prywatny'), (3, 'słżbowy')])),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_box.Person')),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_box.Person'),
        ),
    ]
