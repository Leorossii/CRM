# Generated by Django 4.1.2 on 2022-10-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contatti', '0002_remove_contatto_ruolo_remove_contatto_telefono_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatto',
            name='ruolo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
