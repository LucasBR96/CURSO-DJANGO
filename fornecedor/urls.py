from django.urls import path
from fornecedor import views

app_name = 'fornecedor'
urlpatterns = [
    path('lista_fornecedor/', views.lista_fornecedor, name='lista_fornecedor'),
    path('cadastra_fornecedor/', views.cadastra_fornecedor, name='cadastra_fornecedor'),
    path('remover_forn/', views.remover_forn , name = 'remover_forn')
]