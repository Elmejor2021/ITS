# Generated by Django 3.2.9 on 2021-12-09 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MNombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='NoDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NNombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('NApellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('NOficina', models.CharField(max_length=50, verbose_name='Oficina')),
                ('NEdad', models.IntegerField(verbose_name='Edad')),
                ('Full_Nombre', models.CharField(blank=True, max_length=150, verbose_name='Nombre Completo')),
            ],
            options={
                'verbose_name': 'No Docente',
                'verbose_name_plural': 'No Docentes',
            },
        ),
        migrations.CreateModel(
            name='DocenteCla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('Edad', models.IntegerField(verbose_name='Edad')),
                ('materia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.materia')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'ordering': ['Nombre'],
            },
        ),
    ]
