# Generated by Django 4.2.19 on 2025-03-08 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0002_remove_course_shortname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]
