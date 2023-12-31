# Generated by Django 4.2.4 on 2023-09-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_alter_quote_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.AddField(
            model_name='author',
            name='born_date',
            field=models.CharField(default='01/01/1900'),
        ),
        migrations.RemoveField(
            model_name='quote',
            name='tags',
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='authapp.tag'),
        ),
    ]
