# Generated by Django 2.2.7 on 2020-02-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_auto_20200128_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=10)),
                ('orderId', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('detail', models.CharField(max_length=150)),
            ],
        ),
    ]
