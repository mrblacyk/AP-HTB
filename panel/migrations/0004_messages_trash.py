# Generated by Django 3.0 on 2020-01-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20200124_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='trash',
            field=models.BooleanField(default=False),
        ),
    ]
