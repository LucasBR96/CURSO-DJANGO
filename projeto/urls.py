from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', lambda request : redirect("carrinho/")),
    path('carrinho/', include('carrinho.urls')),
    path('produto/', include('produto.urls')),
    path('admin/', admin.site.urls),
    path('fornecedor/', include('fornecedor.urls'))
]

#     Como acessar a página index.html do projeto:
#     http://127.0.0.1:8000/
#
#     Como acessar a página index.html de produto:
#     http://127.0.0.1:8000/produto/