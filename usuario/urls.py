from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('exibir/', views.exibir, name='exibir'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'),
]
