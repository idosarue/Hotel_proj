# Generated by Django 3.2.6 on 2022-01-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220107_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
