# Generated by Django 4.2.1 on 2023-05-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_name_workobject_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workobject',
            name='user',
        ),
        migrations.RemoveField(
            model_name='worktype',
            name='user',
        ),
    ]
