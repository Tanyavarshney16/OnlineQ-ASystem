# Generated by Django 2.2.1 on 2019-06-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0031_question_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='publish',
            field=models.DateField(null=True),
        ),
    ]
