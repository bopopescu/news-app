# Generated by Django 2.0.8 on 2018-10-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_temppages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temppages',
            name='aboutme',
        ),
        migrations.RemoveField(
            model_name='temppages',
            name='phone',
        ),
        migrations.AddField(
            model_name='temppages',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
