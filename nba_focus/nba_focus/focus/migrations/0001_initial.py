# Generated by Django 2.2.4 on 2019-08-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('title', models.CharField(help_text='Enter a news title', max_length=200, primary_key=True, serialize=False)),
                ('url', models.TextField(help_text='Enter a news url', max_length=1000)),
            ],
        ),
    ]
