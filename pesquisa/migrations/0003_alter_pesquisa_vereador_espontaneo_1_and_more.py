# Generated by Django 5.0.7 on 2024-07-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0002_alter_pesquisa_vereador_espontaneo_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_espontaneo_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_espontaneo_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_espontaneo_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_espontaneo_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_espontaneo_5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_espontaneo_6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='vereador_induzido',
            field=models.ManyToManyField(blank=True, limit_choices_to={'cargo': 'Vereador'}, related_name='pesquisas_vereador_induzido', to='pesquisa.candidato'),
        ),
    ]