# Generated by Django 4.0.10 on 2023-08-20 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_test_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='body',
        ),
    ]
