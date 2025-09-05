from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_plano, name='criar_plano'),
    path('', views.exibir_planos, name='exibir_planos'),
    path('<int:plano_id>/excluir/', views.excluir_plano, name='excluir_plano'),
    path('<int:plano_id>/assinar/', views.assinar_plano, name='assinar_plano'),
]
