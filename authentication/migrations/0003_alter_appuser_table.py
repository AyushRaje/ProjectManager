# Generated by Django 4.2.4 on 2023-08-26 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_user_appuser'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='appuser',
            table='App_users',
        ),
    ]
