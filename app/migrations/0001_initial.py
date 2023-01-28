# Generated by Django 4.1.3 on 2023-01-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomAgence', models.CharField(max_length=45)),
                ('Nature', models.CharField(max_length=20)),
                ('Nif', models.IntegerField()),
                ('RegistreCom', models.CharField(max_length=60)),
                ('AdressePhysique', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=20)),
                ('telephone', models.CharField(max_length=13)),
            ],
        ),
    ]
