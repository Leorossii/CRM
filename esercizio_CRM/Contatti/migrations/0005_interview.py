# Generated by Django 4.1.2 on 2022-10-19 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clienti', '0001_initial'),
        ('Contatti', '0004_remove_contatto_nominativo_contatto_cognome_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clienti.cliente')),
                ('contatto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contatti.contatto')),
            ],
        ),
    ]