# Generated by Django 2.2.1 on 2019-06-11 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_user_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mname',
            field=models.CharField(max_length=20),
        ),
    ]
