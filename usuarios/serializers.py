from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from usuarios.models import Cliente

from rest_framework.serializers import CharField, EmailField, HyperlinkedIdentityField, ModelSerializer, SerializerMethodField, ValidationError

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'sobrenome',
            'nomeUsuario',
            'email',
            'cpf',
            'endereco',
            'telefone',
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='E-mail')
    email2 = EmailField(label='Confirma o e-mail')
    nomeUsuario = CharField(label='Nome de Usuario')
    nome = CharField(label='Primeiro Nome')
    sobrenome = CharField(label='Ultimo Nome')
    cpf = CharField(label='CPF')
    password = CharField(label='Senha')
    endereco = CharField(label='Endereco')
    telefone = CharField(label='Telefone')
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'sobrenome',
            'nomeUsuario',
            'email',
            'email2',
            'cpf',
            'endereco',
            'telefone',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        nome = data['nome']
        sobrenome = data['sobrenome']
        nomeUsuario = data['nomeUsuario']
        email = data['email']
        endereco = data['endereco']
        telefone = data['telefone']
        cpf = data['cpf']
        password = data['password']
        userObj = User(username=nomeUsuario, email=email, first_name=nome, last_name=sobrenome)
        userObj.set_password(password)
        userObj.save()
        clienteObj = Cliente(nome=nome, sobrenome=sobrenome, nomeUsuario=nomeUsuario, email=email, cpf=cpf, endereco=endereco, telefone=telefone)
        clienteObj.save()
        return data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='E-mail', required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        userObj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise ValidationError("E necessario um nome de usuario ou email para o login")
        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            userObj = user.first()
        else:
            raise ValidationError("Nome de usuario ou e-mail invalidos.")
        if userObj:
            if not userObj.check_password(password):
                raise ValidationError("Senha errada.")
        data['token'] = "Algum token aleatorio"
        return data
