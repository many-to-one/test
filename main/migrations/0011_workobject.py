# Generated by Django 4.2.1 on 2023-05-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_work_sum_time_sec_alter_work_diff_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workobject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
