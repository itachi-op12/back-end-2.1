from django.contrib import admin
from django.urls import path, include
from usuario import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('historico/', include('historico.urls')),
    path('plano/', include('plano.urls')),
    path('', usuario_views.home, name='home'),  # raiz
]

