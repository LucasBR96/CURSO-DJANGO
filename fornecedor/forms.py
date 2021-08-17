from fornecedor.models import Fornecedor
from django import forms
import re

# funcoes de validacao --------------------------------------------------------

FIRST_CNPJ_SEQ = [5,4,3,2,9,8,7,6,5,4,3,2]
SECND_CNPJ_SEQ = [6,5,4,3,2,9,8,7,6,5,4,3,2]
DIGITS         = ''.join( map( str , range(10) ) )

TEL_RX1 = r"^\d{2}\s\d{4,5}\s\d{4}$"
TEL_RX2 = r"^\d{11,12}$"
NOME_RX = r"^([A-Z][a-z]+|[a-z])(\s([A-Z][a-z]+|[a-z]))*$"
ENDR_RX = r"^(\w+|\s)+$"

def valida_cnpj( cnpj_str ):

    #-------------------------------------------------
    # filtra os digitos de cnpj_str
    foo = lambda x: x in DIGITS
    cnpj_str = ''.join( filter( foo , cnpj_str ) )
    if len( cnpj_str ) != 14:
        return False
    
    cnpj_digits = list( map( int , [ x for x in cnpj_str ] ) )
    vef1 , vef2 = cnpj_digits[ -2: ]
    base = cnpj_digits[ :12 ]

    #-------------------------------------------------
    # primeira verificação de digitos
    soma = 0
    for x , y in zip( base , FIRST_CNPJ_SEQ ):
        soma += x*y
    res = soma%11
    res = 0 if res < 2 else 11 - res
    if res != vef1:
        return False

    #-------------------------------------------------
    # segunda verificação de digitos
    base.append( vef1 )
    soma = 0
    for x , y in zip( base , SECND_CNPJ_SEQ ):
        soma += x*y
    res = soma%11
    res = 0 if res < 2 else 11 - res
    if res != vef2:
        return False
    
    return True

def valida_telefone( tel_str ):

    m1 = re.match( TEL_RX1 , tel_str ) is not None
    m2 = re.match( TEL_RX2 , tel_str ) is not None
    return m1 or m2

def valida_nome( nome_str ):

    return re.match( TEL_RX1 , nome_str ) is not None

def valida_endr( nome_str ):

    return re.match( TEL_RX1 , nome_str ) is not None

class FornecedorForm( forms.ModelForm ):
    
    class Meta:
        model = Fornecedor
        fields = ( 'Nome' , 'Endereco' , 'Telefone', 'CNPJ' )
    
    Nome = forms.CharField(
        error_messages = { 
            "Required":"campo obrigatório",
            "unique":"Nome duplicado"
        },
        widget = forms.TextInput( attrs = {'class':'form-control form-control-sm', 'max-lenght': '100'})
    )