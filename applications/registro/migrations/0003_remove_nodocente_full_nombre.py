# Generated by Django 3.2.9 on 2021-12-16 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20211209_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodocente',
            name='Full_Nombre',
        ),
    ]
