from django.shortcuts import render

# Create your views here.
def index( request ):
    frase = "essa frase está sendo exibida pelo index.html de produto"
    return render( request , 'produto/index.html', {'frase':frase} )

def pagina1( request ):
    frase = "essa frase está sendo exibida por produto/pagina1.html"
    return render( request , 'produto/pagina1.html', {'frase':frase} )

def pagina2( request ):
    frase = "essa frase está sendo exibida produto/pagina2.html"
    return render( request , 'produto/pagina2.html', {'frase':frase} )