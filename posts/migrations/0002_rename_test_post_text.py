# Generated by Django 4.0.10 on 2023-08-20 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='test',
            new_name='text',
        ),
    ]
