app_name = "carrinho"

from carrinho import views
from django.urls import path, include

urlpatterns = [
    path('',views.lista_produto, name = "lista_produtos"),

    #--------------------------------------------------------
    # carrinho/fruta
    # carrinho/grão
    path('<slug:slug_da_categoria>/', views.lista_produto, name = "lista_produtos_por_categoria"),

    #--------------------------------------------------------
    # carrinho/11/laranja
    # carrinho/21/arroz
    path('<int:id>/<slug:slug_do_produto>/', views.exibe_produto, name = "exibe_produto")
]