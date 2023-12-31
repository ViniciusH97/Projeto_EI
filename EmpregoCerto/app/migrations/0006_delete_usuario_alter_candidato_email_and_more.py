# Generated by Django 4.2.7 on 2023-11-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_cpnj_empresa_cnpj'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AlterField(
            model_name='candidato',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='segmento',
            field=models.CharField(max_length=100),
        ),
    ]
