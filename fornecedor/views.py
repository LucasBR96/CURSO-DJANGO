from django.http.response import JsonResponse
import fornecedor
from django.core.paginator import Paginator
from django.shortcuts import render
from fornecedor.models import Fornecedor
from fornecedor.forms import FornecedorForm
from django.contrib import messages
from django.http import JsonResponse

def mostrar_fornecedor( request , **kwargs ):

    forn = Fornecedor.objects.get( id = kwargs[ "id" ] )
    return render( request , "fornecedor/mostrar.html" , {'form':forn } )

def remover_forn( request ):
    pass

def lista_fornecedor(request):
    lista_de_fornecedores = Fornecedor.objects.all()

    #---------------------------------------------------------
    # Pagina 1 : 1 - 3
    # Pagina 2 : 4 - 6
    paginator = Paginator(lista_de_fornecedores, 4)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    return render(request, 'fornecedor/lista_forn.html', { 'forn': page_obj })

def cadastra_fornecedor( request ):

    if request.POST:
        fornecedor_form = FornecedorForm( data = request.POST )
        if fornecedor_form.is_valid():
            form = fornecedor_form.save()
            # messages.add_message( request , messages.INFO , "fornecedor cadastrado com sucesso" )

            # return render( request , "fornecedor/acpt.html" , {'form':form } )

            return JsonResponse( { "success":True } )
    else:
        fornecedor_form = FornecedorForm()
    return render( request, 'fornecedor/form.html', { 'formulario': fornecedor_form }) 