from django.shortcuts import render
from rest_framework.serializers import IntegerField
from rest_framework import viewsets
from .models import Produto, Estoque
from .serializers import ProdutoSerializer, EstoqueSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsOwnerOrReadOnly
#from responders.permissions import IsAccountAdminOrReadOnly
from django_filters import rest_framework as filters
from django.db.models import Q
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser | IsOwnerOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    def perform_create(self, serializer):
        serializer.save()
        idProduto = serializer.data["id"]
        produto = Produto.objects.filter(Q(id=idProduto)).first()
        estoque = Estoque()
        estoque.produto = produto
        estoque.quantidade = self.request.data["quantidadeInicial"]
        estoque.save()
    def perform_update(self, serializer):
        serializer.save()
        idProduto = serializer.data["id"]
        produto = Produto.objects.filter(Q(id=idProduto)).first()
        estoque = Estoque.objects.filter(Q(produto=produto)).first()
        estoque.quantidade = self.request.data["quantidadeInicial"]
        estoque.save()


class EstoqueViewSet(viewsets.ModelViewSet):
    serializer_class = EstoqueSerializer
    queryset = Estoque.objects.all()
    permission_classes = [IsAdminUser | IsOwnerOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

# Create your views here.
