# Generated by Django 3.0.6 on 2020-09-09 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Muser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Sal', 'Sales'), ('Opn', 'Operations'), ('Fin', 'Finance'), ('Adm', 'Admin')], default='Sal', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('O', 'O'), ('TA', 'TA'), ('TNA', 'TNA'), ('CA', 'CA'), ('CNA', 'CNA'), ('S', 'S')], default='OPEN', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multierp.Muser')),
            ],
        ),
    ]
