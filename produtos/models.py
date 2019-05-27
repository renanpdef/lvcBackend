from django.db import models

class Produto(models.Model):
    CATEGORIAS = (
        ('PR', 'Processadores'),
        ('MR', 'Memoria RAM'),
        ('DR', 'Disco Rigido/SSD'),
        ('PV', 'Placa de Video'),
        ('GA', 'Gabinete'),
        ('PM', 'Placa Mae'),
        ('FO', 'Fonte'),
    )
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, verbose_name='Categoria')
    nome = models.CharField(max_length=30, verbose_name='Nome')
    valor = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Valor')
    descricao = models.TextField(verbose_name='Descricao')
    quantidadeInicial = models.IntegerField(verbose_name='Quantidade Inicial', serialize=False)


    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(verbose_name='Quantidade')

    def __str__(self):
        return self.produto.nome

