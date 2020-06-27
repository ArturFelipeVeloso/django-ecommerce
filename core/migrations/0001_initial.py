# Generated by Django 2.2.6 on 2020-06-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='None')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('Mennsagem', models.TextField()),
                ('send', models.DateTimeField(auto_now_add=True, verbose_name='Enviado em')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
    ]
