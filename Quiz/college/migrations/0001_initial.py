# Generated by Django 2.2.7 on 2020-01-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2)),
                ('section', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fatherName', models.CharField(max_length=30)),
                ('motherName', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('Class', models.IntegerField()),
                ('prevClass', models.IntegerField()),
                ('prevClassMark', models.IntegerField()),
                ('prevResult', models.ImageField(upload_to='images')),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('image', models.ImageField(upload_to='images')),
                ('department', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('rollno', models.CharField(max_length=10)),
            ],
        ),
    ]
