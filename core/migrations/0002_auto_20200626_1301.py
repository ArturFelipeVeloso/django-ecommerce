# Generated by Django 2.2.6 on 2020-06-26 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Mennsagem',
            new_name='message',
        ),
    ]
