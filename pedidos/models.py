from django.db import models
from django.conf import settings
from produtos.models import Produto
from usuarios.models import Cliente

class Pedido(models.Model):
    STATUS = (
        ('PR', 'Pedido Realizado'),
        ('SE', 'Separacao em Estoque'),
        ('EM', 'Em Montagem'),
        ('RT', 'Realizacao de Testes'),
        ('CO', 'Concluido'),
    )
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='+')
    processador = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'PR'}, related_name='+')
    memoria = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'MR'}, related_name='+')
    discoRigido = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'DR'}, related_name='+')
    placaDeVideo = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'PV'}, related_name='+')
    gabinete = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'GA'}, related_name='+')
    placaMae = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'PM'}, related_name='+')
    fonte = models.ForeignKey(Produto, on_delete=models.CASCADE, limit_choices_to={'categoria': 'FO'}, related_name='+')
    status = models.CharField(max_length=2, choices=STATUS, verbose_name='Status', default='PR', editable=False)

    @property
    def valor(self):
        valorTotal = self.processador.valor + self.memoria.valor + self.discoRigido.valor + self.placaDeVideo.valor + self.gabinete.valor + self.placaMae.valor + self.fonte.valor
        return valorTotal
    # def __str__(self):
    #     return self.nome
