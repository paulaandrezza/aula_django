from django.urls import include, path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('listar/', views.listar, name="listar"),
    path('listar/<int:id>', views.listar_unico, name="listar_unico"),
]
