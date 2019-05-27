from django.shortcuts import render
from rest_framework import viewsets
from .models import Pedido
from produtos.models import Produto
from usuarios.models import Cliente
from django.db.models import Q
from .serializers import PedidoSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from rest_framework.response import Response
from trello import trelloApi
from rest_framework.serializers import ValidationError
from rest_framework import status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication




class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = self.request.user
        cliente = Cliente.objects.filter(Q(email=user.email)).first()
        if (cliente == None):
            print("ENTROU")
            return Response("Administradores nao podem realizar pedidos.")
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, cliente)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, cliente):
        serializer.save(user=cliente)
        data = self.request.data
        processador = Produto.objects.filter(Q(id=data["processador"])).first().nome
        memoria = Produto.objects.filter(Q(id=data["memoria"])).first().nome
        discoRigido = Produto.objects.filter(Q(id=data["discoRigido"])).first().nome
        placaDeVideo = Produto.objects.filter(Q(id=data["placaDeVideo"])).first().nome
        gabinete = Produto.objects.filter(Q(id=data["gabinete"])).first().nome
        placaMae = Produto.objects.filter(Q(id=data["placaMae"])).first().nome
        fonte = Produto.objects.filter(Q(id=data["fonte"])).first().nome
        idPedido = Pedido.objects.filter(Q(user=cliente)).last().id
        nome = str(cliente.nome) + " " + str(cliente.sobrenome)
        email = cliente.email
        telefone = cliente.telefone
        trelloApi.adicionarPedido(idPedido, nome, email, telefone, processador, memoria, discoRigido, placaDeVideo, gabinete, placaMae, fonte)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        statusPedidos = trelloApi.obterStatusPedidos()
        for i in range(0,len(serializer.data)):
            idPedido = serializer.data[i]["id"]
            nomePedido = "Pedido " + str(idPedido)
            if (nomePedido in statusPedidos):
                pedido = Pedido.objects.filter(Q(id=idPedido)).first()
                if (pedido.status != statusPedidos[nomePedido]):
                    pedido.status = statusPedidos[nomePedido]
                    pedido.save()
                    queryset = self.filter_queryset(self.get_queryset())
                    serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        statusPedidos = trelloApi.obterStatusPedidos()
        idPedido = serializer.data["id"]
        nomePedido = "Pedido " + str(idPedido)
        if(nomePedido in statusPedidos):
            pedido = Pedido.objects.filter(Q(id=idPedido)).first()
            if(pedido.status != statusPedidos[nomePedido]):
                pedido.status = statusPedidos[nomePedido]
                pedido.save()
                instance = self.get_object()
                serializer = self.get_serializer(instance)
        return Response(serializer.data)