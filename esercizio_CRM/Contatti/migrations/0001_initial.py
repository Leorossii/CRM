# Generated by Django 4.1.2 on 2022-10-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contatto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominativo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('ruolo', models.CharField(max_length=100)),
            ],
        ),
    ]
