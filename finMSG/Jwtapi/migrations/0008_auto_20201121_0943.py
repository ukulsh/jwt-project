# Generated by Django 3.0.7 on 2020-11-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jwtapi', '0007_auto_20200908_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotapiQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencetoken', models.CharField(max_length=60)),
                ('question', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'chatbotapi_query',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='JwtapiQuery',
        ),
    ]