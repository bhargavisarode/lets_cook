# Generated by Django 3.0.8 on 2020-12-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201214_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_course',
            field=models.BooleanField(default=False),
        ),
    ]
