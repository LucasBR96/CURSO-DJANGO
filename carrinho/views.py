from django.shortcuts import render, get_object_or_404
from produto.models import Produto
from categoria.models import Categoria
# Create your views here.

def lista_produto( request , slug_da_categoria = None ):
    
    cat = None
    produtos = Produto.objects.filter( disponivel = True ).order_by('nome')
    if not ( slug_da_categoria is None ):
        cat = get_object_or_404( Categoria , slug = slug_da_categoria )
        produtos = produtos.filter( categoria = cat )
    
    categorias = Categoria.objects.all().order_by('nome')
    
    d = dict()
    d['categorias'] = categorias
    d['produtos']   = produtos
    d['cat']        = cat

    return render( request, 'carrinho/lista_produtos.html', d )

def exibe_produto( request , id , slug_do_produto ):
    pass
