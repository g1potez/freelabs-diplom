# Generated by Django 3.2.12 on 2022-02-17 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynewuser', '0002_rename_users_db_freelabs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='db_freelabs',
        ),
    ]
