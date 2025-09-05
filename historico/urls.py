from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_consulta, name='criar_consulta'),
    path('<int:consulta_id>/', views.exibir_consulta, name='exibir_consulta'),
    path('', views.listar_consultas, name='listar_consultas'),
    path('<int:consulta_id>/excluir/', views.excluir_consulta, name='excluir_consulta'),
]
