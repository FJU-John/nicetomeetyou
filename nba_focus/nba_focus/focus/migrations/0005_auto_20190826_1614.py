# Generated by Django 2.2.4 on 2019-08-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0004_auto_20190826_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.CharField(blank=True, help_text='Enter a time', max_length=200, null=True),
        ),
    ]