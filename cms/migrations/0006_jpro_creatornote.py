# Generated by Django 3.0.4 on 2020-04-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_jpro'),
    ]

    operations = [
        migrations.AddField(
            model_name='jpro',
            name='creatornote',
            field=models.CharField(blank=True, max_length=255, verbose_name='著者紹介'),
        ),
    ]
