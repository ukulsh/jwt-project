# Generated by Django 3.0.7 on 2020-09-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jwtapi', '0004_auto_20200826_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intents',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='uuid',
        ),
    ]
