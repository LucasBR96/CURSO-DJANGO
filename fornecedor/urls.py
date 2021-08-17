from django.urls import path
from fornecedor import views

app_name = 'fornecedor'
urlpatterns = [
    path('lista_fornecedor/', views.lista_fornecedor, name='lista_fornecedor')
]