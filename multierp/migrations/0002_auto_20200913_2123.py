# Generated by Django 3.0.6 on 2020-09-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multierp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ManyToManyField(to='multierp.Muser'),
        ),
    ]