# Generated by Django 5.1.7 on 2025-04-08 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user_role',
        ),
    ]
