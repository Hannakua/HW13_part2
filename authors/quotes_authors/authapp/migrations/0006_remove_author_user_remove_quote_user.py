# Generated by Django 4.2.4 on 2023-09-03 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_remove_quote_quote_for_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
    ]
