# Generated by Django 2.2.4 on 2019-08-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
    ]