from django.contrib import admin
from django.urls import path, include
from usuario import views as usuario_views  # importa views do app usuario

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/", include("usuario.urls")),
    path("historico/", include("historico.urls")),
    path("plano/", include("plano.urls")),

    # raiz do site redirecionando para login
    path("", usuario_views.login_view, name="home"),
]
