from django.urls import include, path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
]
