# Generated by Django 4.0.2 on 2022-03-07 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='s',
        ),
    ]