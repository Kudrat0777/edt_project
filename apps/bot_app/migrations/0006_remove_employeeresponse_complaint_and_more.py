# Generated by Django 4.2.10 on 2024-02-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0005_alter_civilcomplaint_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeresponse',
            name='complaint',
        ),
        migrations.DeleteModel(
            name='CivilComplaint',
        ),
        migrations.DeleteModel(
            name='EmployeeResponse',
        ),
    ]
