# Generated by Django 4.2.2 on 2023-07-08 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='fathers_img',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='mothers_img',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='student_img',
        ),
    ]
