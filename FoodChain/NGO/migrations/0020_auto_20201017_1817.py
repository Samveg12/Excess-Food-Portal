# Generated by Django 3.1 on 2020-10-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0019_auto_20201017_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodavbl',
            name='pickup_address',
            field=models.TextField(max_length=200),
        ),
    ]