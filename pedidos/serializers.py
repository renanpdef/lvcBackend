from rest_framework import serializers
from .models import Pedido
from produtos.models import Estoque
from trello import trelloApi
from usuarios.serializers import UserDetailSerializer, ValidationError
from django.db.models import Q
# from django.contrib.auth import get_user_model
# User = get_user_model()

class PedidoSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Pedido
        fields = [
            'id',
            'user',
            'processador',
            'memoria',
            'discoRigido',
            'placaDeVideo',
            'gabinete',
            'placaMae',
            'fonte',
            'status',
            'valor',
        ]

    def validate(self, data):
        processador = data['processador']
        memoria = data['memoria']
        discoRigido = data['discoRigido']
        placaDeVideo = data['placaDeVideo']
        gabinete = data['gabinete']
        placaMae = data['placaMae']
        fonte = data['fonte']
        prEstoque = Estoque.objects.filter(Q(produto=processador)).first()
        if(prEstoque.quantidade > 0):
            prEstoque.quantidade -= 1
            prEstoque.save()
        else:
            raise ValidationError("Processador indisponivel.")

        mrEstoque = Estoque.objects.filter(Q(produto=memoria)).first()
        if (mrEstoque.quantidade > 0):
            mrEstoque.quantidade -= 1
            mrEstoque.save()
        else:
            raise ValidationError("Memoria indisponivel.")

        drEstoque = Estoque.objects.filter(Q(produto=discoRigido)).first()
        if (drEstoque.quantidade > 0):
            drEstoque.quantidade -= 1
            drEstoque.save()
        else:
            raise ValidationError("Disco Rigido/SSD indisponivel.")

        pvEstoque = Estoque.objects.filter(Q(produto=placaDeVideo)).first()
        if (pvEstoque.quantidade > 0):
            pvEstoque.quantidade -= 1
            pvEstoque.save()
        else:
            raise ValidationError("Placa de Video indisponivel.")

        gaEstoque = Estoque.objects.filter(Q(produto=gabinete)).first()
        if (gaEstoque.quantidade > 0):
            gaEstoque.quantidade -= 1
            gaEstoque.save()
        else:
            raise ValidationError("Gabinete indisponivel.")

        pmEstoque = Estoque.objects.filter(Q(produto=placaMae)).first()
        if (pmEstoque.quantidade > 0):
            pmEstoque.quantidade -= 1
            pmEstoque.save()
        else:
            raise ValidationError("Placa Mae indisponivel.")

        foEstoque = Estoque.objects.filter(Q(produto=fonte)).first()
        if (foEstoque.quantidade > 0):
            foEstoque.quantidade -= 1
            foEstoque.save()
        else:
            raise ValidationError("Fonte indisponivel.")

        return data

