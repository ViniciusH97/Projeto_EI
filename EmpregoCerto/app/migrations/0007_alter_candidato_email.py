# Generated by Django 4.2.7 on 2023-11-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_usuario_alter_candidato_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
