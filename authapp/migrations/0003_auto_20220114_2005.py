# Generated by Django 3.2.7 on 2022-01-14 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_activation_expires_shopuser_activation_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='activation_expires',
        ),
        migrations.RemoveField(
            model_name='shopuser',
            name='activation_key',
        ),
    ]
