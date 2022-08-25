from django.conf.urls import include, url
from django.urls import path
from . import views

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter
from perfis import views

router = DefaultRouter()
router.register('perfis', views.PerfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('', views.index, name='index'),
    path('perfil/', views.get_meu_perfil, name='perfil'),
    path('convites/', views.get_convites, name='convites'),
    path('convites/convidar/<int:perfil_id>', views.convidar, name='convidar'),
    path('convites/aceitar/<int:convite_id>', views.aceitar, name='aceitar'),
    path('login/', auth_views.obtain_auth_token, name='login')
]
