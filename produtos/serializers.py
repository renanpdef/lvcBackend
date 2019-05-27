from rest_framework import serializers
from django.db.models import Q
from .models import Produto, Estoque

# class ProdutoDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Produto
#         fields = [
#             'id',
#             'categoria',
#             'nome',
#             'valor',
#             'descricao',
#         ]

class ProdutoSerializer(serializers.ModelSerializer):
    quantidadeInicial = serializers.IntegerField(label='Quantidade em Estoque', write_only=True)
    class Meta:
        model = Produto
        fields = '__all__'



class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = [
            'id',
            'produto',
            'quantidade',
        ]
