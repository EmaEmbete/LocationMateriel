# Generated by Django 4.1.3 on 2023-01-28 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_fournisseur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approvisionnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codeappro', models.IntegerField()),
                ('Dateappro', models.DateField()),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur')),
            ],
        ),
    ]
