# Generated by Django 3.0.3 on 2020-03-01 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_server', '0002_auto_20200301_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author',
        ),
    ]