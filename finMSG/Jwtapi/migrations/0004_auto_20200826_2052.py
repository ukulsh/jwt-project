# Generated by Django 3.0.7 on 2020-08-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jwtapi', '0003_auto_20200824_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
