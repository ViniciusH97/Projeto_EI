# Generated by Django 4.2.7 on 2023-11-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_nome_vaga_titulo_remove_vaga_salario'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='area',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
