from django.http.response import JsonResponse
import fornecedor
from django.core.paginator import Paginator
from django.shortcuts import render , redirect , get_object_or_404
from fornecedor.models import Fornecedor
from fornecedor.forms import FornecedorForm , FornSelect
from django.contrib import messages
from django.http import JsonResponse

def mostrar_fornecedor( request , **kwargs ):

    forn = Fornecedor.objects.get( id = kwargs[ "id" ] )
    return render( request , "fornecedor/mostrar.html" , {'forn':forn.get_visual_tuple() } )

def remover_forn( request ):
    
    form = FornSelect( request.POST )
    print( form )
    if form.is_valid():
        forn_id = form.cleaned_data[ 'forn_id' ]
        forn = get_object_or_404( Fornecedor , pk = forn_id)
        forn.Logo.delete()
        forn.delete()

        return redirect( '../lista_fornecedor/' )
    
def edita_fornecedor( request , **kwargs ):
    
    fornecedor_edit = Fornecedor.objects.get( id = kwargs[ "id" ] )
    fornecedor_edit_form = FornecedorForm( instance = fornecedor_edit )
    request.session[ 'forn_id' ] = kwargs["id"]

    return render( request , "fornecedor/form.html" , {"formulario": fornecedor_edit_form} )

def buscar_fornecedor( request , nome ):

    resp = dict()
    try:
        fornec = Fornecedor.objects.get( Nome = nome )
        resp[ 'valid' ] = True
        resp[ 'id' ]    = fornec.id

    except Fornecedor.DoesNotExist:
        resp[ 'valid' ] = False

    return JsonResponse( resp )
    
def lista_fornecedor(request):

    #---------------------------------------------------------
    # Caso o usuario der um clickout de edita fornecedor
    forn_id = request.session.get( 'forn_id' )
    if forn_id:
        del request.session[ 'forn_id' ]

    foo = lambda x : x.get_card_tuple()
    lista_de_fornecedores = [ foo( x ) for x in Fornecedor.objects.all() ]

    #---------------------------------------------------------
    # Pagina 1 : 1 - 3
    # Pagina 2 : 4 - 6
    paginator = Paginator(lista_de_fornecedores, 4)
    pagina = request.GET.get('pagina')
    page_obj = paginator.get_page(pagina)

    return render(request, 'fornecedor/lista_forn.html', { 'forn': page_obj })

def cadastra_fornecedor( request ):

    
    if request.POST:

        print( request.FILES )
        
        forn_id = request.session.get( 'forn_id' )
        #------------------------------------------------------
        # Alterando um fornecedor ja cadastrado
        if forn_id:
            fornec = get_object_or_404( Fornecedor , pk = forn_id )
            fornecedor_form = FornecedorForm( data = request.POST, files = request.FILES, instance = fornec )
            del request.session['forn_id']

        #----------------------------------------------------
        # adicionando um novo fornecedor
        else:
            fornecedor_form = FornecedorForm( data = request.POST, files = request.FILES )
            print( fornecedor_form )

        if fornecedor_form.is_valid():

            #-----------------------------------------------------
            # Vai fazer um SQL insert se o fornecedor for novo, e 
            # um SQL update se for um produto alterado.
            form = fornecedor_form.save()
            msg = "fornecedor adicionado com sucesso"
            if forn_id:
                msg = "fornecedor alterado com sucesso"
            messages.add_message(request, messages.SUCCESS, msg )
    else:
        fornecedor_form = FornecedorForm()
    return render( request, 'fornecedor/form.html', { 'formulario': fornecedor_form }) 