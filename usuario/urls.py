from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


urlpatterns = [
   
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]


urlpatterns = [
    path("", views.login_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("perfil/", views.perfil, name="perfil"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
