from django.urls import path
from .views import home, myLogout

urlpatterns = [
    path('', home, name="home"),
    path('logout', myLogout, name="logout"),
]
