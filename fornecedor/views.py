from django.core.paginator import Paginator
from django.shortcuts import render
from fornecedor.models import Fornecedor

def lista_fornecedor(request):
    lista_de_fornecedores = Fornecedor.objects.all()

    #---------------------------------------------------------
    # Pagina 1 : 1 - 3
    # Pagina 2 : 4 - 6
    paginator = Paginator(lista_de_fornecedores, 4)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    return render(request, 'fornecedor/lista_forn.html', { 'forn': page_obj })