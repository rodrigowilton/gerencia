# Generated by Django 5.0.7 on 2024-07-28 12:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0007_remove_candidato_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesquisa',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]