# Generated by Django 2.1.5 on 2019-03-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newdata',
            name='empid',
        ),
        migrations.RemoveField(
            model_name='newdata',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='newdata',
            name='lastname',
        ),
        migrations.AddField(
            model_name='newdata',
            name='Task',
            field=models.CharField(default='Null value', max_length=100),
        ),
    ]