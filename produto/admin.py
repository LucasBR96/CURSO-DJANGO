from django.contrib import admin
from .models import Produto

class ProdutoAdmin( admin.ModelAdmin ):

    #------------------------------------------------------------------
    # Quais campos podem ser editados a partir da pagina de produtos
    fields = ('categoria', 'nome', 'slug', 'img' , 'qtd_est' , 'preco', 'disponivel')

    #------------------------------------------------------------------
    # quais campos serão listados na tabela da pagina admin
    list_display = ['categoria', 'nome', 'slug', 'img' , 'qdt_est' , 'preco', 'disponivel']

    #------------------------------------------------------------------
    # quais campos que se pode fazer busca
    search_fields = ['nome']

    
# Register your models here.
admin.site.register( Produto , ProdutoAdmin)
