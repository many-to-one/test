# Generated by Django 4.2.1 on 2023-05-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_work_user_remove_workobject_user'),
        ('users', '0003_customuser_fp_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='work_objects',
            field=models.ManyToManyField(to='main.workobject'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='work_type',
            field=models.ManyToManyField(to='main.worktype'),
        ),
    ]
