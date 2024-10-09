# Generated by Django 5.0.4 on 2024-10-09 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('segmento', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'modulos',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'perfiles',
            },
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='firsname',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='numberphome',
        ),
        migrations.AddField(
            model_name='usuario',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numberphone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField(default=1)),
                ('modulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seguridad.modulo')),
                ('perfil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seguridad.perfil')),
            ],
            options={
                'db_table': 'accesos',
            },
        ),
    ]
