# Generated by Django 2.2.7 on 2019-12-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managequestion',
            name='correct_answer',
            field=models.CharField(max_length=2),
        ),
    ]
