# Generated by Django 3.0.8 on 2020-12-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slider_post',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
