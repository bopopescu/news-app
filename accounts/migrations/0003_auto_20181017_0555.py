# Generated by Django 2.0.8 on 2018-10-17 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_temppages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temppages',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='temppages',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='temppages',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='temppages',
            name='updated_by',
        ),
    ]
