# Generated by Django 3.2.12 on 2022-04-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
    ]
