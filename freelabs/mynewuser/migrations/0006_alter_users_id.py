# Generated by Django 3.2.12 on 2022-02-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewuser', '0005_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
