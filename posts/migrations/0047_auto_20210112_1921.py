# Generated by Django 3.1.4 on 2021-01-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0046_auto_20210112_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='disc',
            field=models.BooleanField(default=False, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='category',
            name='more',
            field=models.BooleanField(blank=True, default=False, verbose_name='For Add In Right Menu'),
        ),
    ]
