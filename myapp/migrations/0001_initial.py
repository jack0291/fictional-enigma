# Generated by Django 4.0.4 on 2022-04-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Contact_no', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
