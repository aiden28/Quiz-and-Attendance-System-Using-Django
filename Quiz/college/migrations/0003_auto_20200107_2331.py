# Generated by Django 2.2.7 on 2020-01-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_class_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fatherName', models.CharField(max_length=30)),
                ('motherName', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('Class', models.IntegerField()),
                ('section', models.CharField(max_length=2)),
                ('prevClass', models.IntegerField()),
                ('prevClassMark', models.IntegerField()),
                ('prevResult', models.ImageField(upload_to='images')),
                ('gender', models.CharField(max_length=6)),
                ('image', models.ImageField(upload_to='images')),
                ('department', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('rollno', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'classes'},
        ),
        migrations.AddField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Class'),
        ),
    ]