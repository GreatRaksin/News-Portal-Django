# Generated by Django 3.0.2 on 2020-02-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200202_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ocatid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]
