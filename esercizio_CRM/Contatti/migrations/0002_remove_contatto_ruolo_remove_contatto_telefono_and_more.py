# Generated by Django 4.1.2 on 2022-10-10 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clienti', '0001_initial'),
        ('Contatti', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contatto',
            name='ruolo',
        ),
        migrations.RemoveField(
            model_name='contatto',
            name='telefono',
        ),
        migrations.AddField(
            model_name='contatto',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Clienti.cliente'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=10)),
                ('contatto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contatti.contatto')),
            ],
        ),
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('contatto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contatti.contatto')),
            ],
        ),
    ]
