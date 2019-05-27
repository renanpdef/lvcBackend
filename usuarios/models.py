from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    nomeUsuario = models.CharField(max_length=30, verbose_name='Nome de Usuario')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    endereco = models.CharField(max_length=200, verbose_name='Endereco')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')

    def __str__(self):
        return self.nome