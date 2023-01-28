# Generated by Django 4.1.3 on 2023-01-28 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_detailapprovionnement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datepayement', models.DateField()),
                ('Motif', models.CharField(max_length=50)),
                ('Bordereau', models.FileField(upload_to='')),
                ('Codepayement', models.IntegerField()),
                ('etat', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commande')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.responsable')),
            ],
        ),
    ]
