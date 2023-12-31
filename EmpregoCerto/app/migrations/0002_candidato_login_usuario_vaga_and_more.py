# Generated by Django 4.2.7 on 2023-11-13 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=40)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.login')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=14)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario_procuraemprego',
            name='desempregado',
        ),
        migrations.DeleteModel(
            name='Desempregado',
        ),
        migrations.DeleteModel(
            name='Usuario_procuraEmprego',
        ),
        migrations.AddField(
            model_name='candidato',
            name='vaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vaga'),
        ),
    ]
