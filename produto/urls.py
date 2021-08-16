from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('lista_produto/', views.lista_produto, name='lista_produto')
]