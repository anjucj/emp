# Generated by Django 3.2.15 on 2022-08-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('ecompany', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=200)),
                ('sreg', models.CharField(max_length=200)),
                ('smark', models.CharField(max_length=15)),
            ],
        ),
    ]
