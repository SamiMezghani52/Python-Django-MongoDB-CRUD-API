# Generated by Django 3.2.6 on 2021-08-24 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='Departments',
            new_name='Department',
        ),
    ]
