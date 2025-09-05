from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('<int:user_id>/', views.exibir_usuario, name='exibir_usuario'),
    path('<int:user_id>/excluir/', views.excluir_usuario, name='excluir_usuario'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
