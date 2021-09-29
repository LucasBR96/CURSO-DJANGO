from django.urls import path
from fornecedor import views
from django.shortcuts import redirect

app_name = 'fornecedor'
urlpatterns = [
    path('' , lambda request : redirect('lista_fornecedor/') ),
    path('lista_fornecedor/', views.lista_fornecedor, name='lista_fornecedor'),
    path('cadastra_fornecedor/', views.cadastra_fornecedor, name='cadastra_fornecedor'),
    path('remover_forn/', views.remover_forn , name = 'remover_forn'),
    path('visualisar_fornecedor/<int:id>', views.mostrar_fornecedor ),
    path('edita_fornecedor/<int:id>', views.edita_fornecedor , name = 'edita_fornecedor'),
    path('buscar_fornecedor/<str:nome>' , views.buscar_fornecedor)
]