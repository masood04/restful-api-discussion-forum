# Generated by Django 4.0.2 on 2022-03-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0003_alter_question_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]