# Generated by Django 3.0.6 on 2020-11-06 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multierp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemgroup',
            old_name='group_codee',
            new_name='group_code',
        ),
    ]