from django.shortcuts import render, get_object_or_404
from produto.models import Produto
from categoria.models import Categoria
from carrinho.carrinho import Carrinho
from carrinho.forms import QuantidadeForm
# Create your views here.

def lista_produto( request , slug_da_categoria = None ):
    
    cat = None
    produtos = Produto.objects.filter( disponivel = True ).order_by('nome')
    if not ( slug_da_categoria is None ):
        cat = get_object_or_404( Categoria , slug = slug_da_categoria )
        produtos = produtos.filter( categoria = cat )
    
    categorias = Categoria.objects.all().order_by('nome')
    carr       = Carrinho( request )
    lst_form   = []
    for produto in produtos:
        qtd = carr.get_quantidade( produto.id )
        lst_form.append( QuantidadeForm( initial = {'quantidade':qtd , 'produto_id':produto.id}) )
    
    listas = zip( produtos , lst_form )
    d = dict()
    d['categorias'] = categorias
    d['listas']     = listas
    d['cat']        = cat

    return render( request, 'carrinho/lista_produtos.html', d )

def exibe_produto( request , id , slug_do_produto ):

    #----------------------------------------------
    # slug do produto na real não será usado para nada
    # so ta ai para os motores de busca

    produto = get_object_or_404( Produto , id = id )
    return render( request , 'carrinho/exibe_produto.html', { "produto":produto } )
    
def atualiza_carrinho( request ):
    
    form = QuantidadeForm( request.POST )
    if form.is_valid():
        
        produto_id = form.cleaned_data[ 'produto_id' ]
        quantidade = form.cleaned_data[ 'quantidade' ]

        quantidade += 1
