from django.shortcuts import render


#----------------------------------------------------------------
# Esse método será executado quando chegar uma requisição para 
# https:\\127.0.0.1\ ( localhost )
def index(request):
    frase  = "Esta frase está sendo exibida pela página index.html"
    frase2 = "Esta tbm esta sendo exibida"
    d = { "frase":frase , "frase2":frase2 }
    #              Objeto    Pagina         O que vai ser jogado na pagina
    return render(request, 'index.html', d)