from os import stat
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from projeto import views, settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request : redirect("fornecedor/")),
    path('carrinho/', include('carrinho.urls')),
    path('produto/', include('produto.urls')),
    path('admin/', admin.site.urls),
    path('fornecedor/', include('fornecedor.urls'))
]

#----------------------------------------------------------
# Para o upload de imagens
if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )


#     Como acessar a página index.html do projeto:
#     http://127.0.0.1:8000/
#
#     Como acessar a página index.html de produto:
#     http://127.0.0.1:8000/produto/