# Generated by Django 3.2.8 on 2021-11-06 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='adress',
            new_name='address',
        ),
    ]