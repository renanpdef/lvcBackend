# Generated by Django 2.2.1 on 2019-05-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('nomeUsuario', models.CharField(max_length=30, verbose_name='Nome de Usuario')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereco')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
            ],
        ),
    ]
