from django.core.paginator import Paginator
from django.shortcuts import render
from produto.models import Produto

def lista_produto(request):
    lista_de_produtos = Produto.objects.all().order_by('nome')

    #---------------------------------------------------------
    # Pagina 1 : 1 - 3
    # Pagina 2 : 4 - 6
    paginator = Paginator(lista_de_produtos, 3)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    print(lista_de_produtos)
    print(page_obj)

    return render(request, 'produto/pesquisa_produto.html', { 'produtos': page_obj })