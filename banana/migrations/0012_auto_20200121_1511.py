# Generated by Django 3.0.2 on 2020-01-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banana', '0011_auto_20200121_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_chat',
            name='userId',
            field=models.CharField(default='None', max_length=20),
        ),
    ]