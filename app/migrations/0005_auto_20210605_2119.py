# Generated by Django 3.2.3 on 2021-06-06 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210605_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artista',
            options={'verbose_name': 'Artista', 'verbose_name_plural': 'Artistas'},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='obra',
            options={'verbose_name': 'Obra', 'verbose_name_plural': 'Obras'},
        ),
        migrations.AlterModelOptions(
            name='registro',
            options={'verbose_name': 'Registro', 'verbose_name_plural': 'Registros'},
        ),
    ]