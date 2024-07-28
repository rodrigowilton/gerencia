# Generated by Django 5.0.7 on 2024-07-28 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0005_remove_pesquisa_vereador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesquisa',
            name='prefeito',
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='vereador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pesquisas_prefeito', to='pesquisa.candidato'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='pesquisadora',
            field=models.CharField(choices=[('P1', 'Pesquisador 1'), ('P2', 'Pesquisador 2'), ('P3', 'Pesquisador 3'), ('P4', 'Pesquisador 4'), ('P5', 'Pesquisador 5'), ('P6', 'Pesquisador 6')], max_length=2),
        ),
    ]
