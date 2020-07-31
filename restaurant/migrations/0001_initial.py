# Generated by Django 3.0.8 on 2020-07-31 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Restaurant')),
            ],
            options={
                'db_table': 'menus',
            },
        ),
    ]
