"""lvcBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
# from clientes.views import ClienteViewSet
from produtos.views import ProdutoViewSet, EstoqueViewSet
from pedidos.views import PedidoViewSet
from usuarios.views import UserCreateAPIView, UserLoginAPIView
from django.contrib.auth import views as auth_views
from home import urls as homeUrls

router = routers.DefaultRouter()
#router.register('cliente', ClienteViewSet, base_name='cliente')
router.register('produto', ProdutoViewSet, base_name='produto')
router.register('estoque', EstoqueViewSet, base_name='estoque')
router.register('pedido', PedidoViewSet, base_name='pedido')

urlpatterns = [
    path('', include(homeUrls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/token/', obtain_jwt_token),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('usuario/cadastro/', UserCreateAPIView.as_view(),name='cadastro'),
    path('usuario/login/', UserLoginAPIView.as_view(),name='loginUser'),

]
