from django.contrib import admin
from .models import Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
    fields = ( 'Nome', 'Endereco', 'Telefone', 'CNPJ' )
    list_display = [ 'Nome', 'Endereco', 'Telefone', 'CNPJ' ]
    search_fields = ['Nome', 'CNPJ']
    list_editable = [ 'Endereco', 'Telefone', 'CNPJ']
    #prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Fornecedor, FornecedorAdmin)