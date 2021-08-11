from django.shortcuts import render


#----------------------------------------------------------------
# Esse método será executado quando chegar uma requisição para 
# https:\\127.0.0.1\ ( localhost )
def index(request):
    return render(request, 'index.html')