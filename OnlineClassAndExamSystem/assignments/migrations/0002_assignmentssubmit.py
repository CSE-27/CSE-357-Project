# Generated by Django 3.2.9 on 2022-01-13 06:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentsSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=50)),
                ('studentId', models.CharField(max_length=100)),
                ('questionFile', models.FileField(upload_to='files/%y')),
                ('answerFile', models.FileField(upload_to='files/%y')),
                ('submitTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
