from fornecedor.models import Fornecedor
from django import forms
import re

# funcoes de validacao --------------------------------------------------------

FIRST_CNPJ_SEQ = [5,4,3,2,9,8,7,6,5,4,3,2]
SECND_CNPJ_SEQ = [6,5,4,3,2,9,8,7,6,5,4,3,2]
VALID        = 0 #CNPJ valido
FORM_INVALID = 1 #O String para o CNPJ não é composto por 14 digitos
NUMR_INVALID = 2 #Os 12 primeiros digitos não validam os dois ultimos 

CNPJ_RX = r"^\d{14}$"
TEL_RX2 = r"^\d{11,12}$"
ENDR_RX = r"^(\w+|\s)+$"

def verifica_digitos( base , ref , vef ):

    soma = 0
    for x , y in zip( base , ref ):
        soma += x*y
    res = soma%11
    res = 0 if res < 2 else 11 - res
    return ( res == vef )

def valida_cnpj( cnpj_str ):

    #-------------------------------------------------
    # filtra os digitos de cnpj_str
    if re.match( CNPJ_RX , cnpj_str ) is None:
        return FORM_INVALID
    
    cnpj_digits = list( map( int , [ x for x in cnpj_str ] ) )
    vef1 , vef2 = cnpj_digits[ -2: ]
    base = cnpj_digits[ :12 ]

    #-------------------------------------------------
    # primeira verificação de digitos
    a = verifica_digitos( base , FIRST_CNPJ_SEQ, vef1 )

    #-------------------------------------------------
    # segunda verificação de digitos
    base.append( vef1 )
    b = verifica_digitos( base , SECND_CNPJ_SEQ , vef2 )
    
    if not ( a and b ): return NUMR_INVALID
    return VALID

def valida_telefone( tel_str ):

    # m1 = re.match( TEL_RX1 , tel_str ) is not None
    # m2 = re.match( TEL_RX2 , tel_str ) is not None
    # return m1 or m2

    return re.match( TEL_RX2 , tel_str ) is not None

def valida_nome_endr( nome_str ):

    #----------------------------------------------
    # nome e endereço aceitam a mesma regex
    return re.match( ENDR_RX , nome_str ) is not None


class FornecedorForm( forms.ModelForm ):

    
    class Meta:
        model = Fornecedor
        fields = ( 'Nome' , 'Endereco' , 'Telefone', 'CNPJ' , 'Logo' )
    
    Nome = forms.CharField(
        error_messages = { 
            "required":"Campo obrigatório",
            "unique":"Nome duplicado"
        },
        widget = forms.TextInput( attrs = {'class':'form-control form-control-sm', 'max-lenght': '100'})
    )

    Endereco = forms.CharField(
        error_messages = { 
            "required":"Campo obrigatório",
            "unique":"Endereco duplicado"
        },
        widget = forms.TextInput( attrs = {'class':'form-control form-control-sm', 'max-lenght': '100'})
    )

    Telefone = forms.CharField(
        error_messages = { 
            "required":"Campo obrigatório",
            "unique":"Telefone duplicado"
        },
        widget = forms.TextInput( attrs = {'class':'form-control form-control-sm', 'max-lenght': '25'})
    )

    CNPJ = forms.CharField(
        error_messages = { 
            "required":"Campo obrigatório",
            "unique":"CNPJ duplicado"
        },
        widget = forms.TextInput( attrs = {'class':'form-control form-control-sm', 'max-lenght': '30'})
    )

    Logo = forms.ImageField(
        error_messages = {
        },
        widget = forms.ClearableFileInput( attrs = { 'class':'btn btn-outline-primary btn-sm'})
    )

    def clean_Telefone( self ):

        tel_str = self.cleaned_data[ 'Telefone' ]
        if not valida_telefone( tel_str ):
            raise forms.ValidationError( 'Telefone inválido: o numero deve ter entre 11 e 12 dígitos')
        return tel_str
    
    def clean_CNPJ( self ):

        
        cnpj_str = self.cleaned_data[ 'CNPJ' ]
        res = valida_cnpj( cnpj_str )
        if res == VALID:
            return cnpj_str

        s = "CNPJ inválido:"
        if res == FORM_INVALID:
            s += " apenas dígitos"
            print( "!" )
        elif res == NUMR_INVALID:
            s += " os dois ultimos digitos não validam os 12 primeiros"
        raise forms.ValidationError( s )
    
    def clean_Endereco( self ):

        addr_str = self.cleaned_data[ 'Endereco' ]
        if valida_nome_endr( addr_str ):
            return addr_str
        
        raise forms.ValidationError( 'Endereco invalido: Apenas letras, números e espaços')

    def clean_Nome( self ):

        nome_str = self.cleaned_data[ 'Nome' ]
        if valida_nome_endr( nome_str ):
            return nome_str
        
        raise forms.ValidationError( 'Nome invalido: Apenas letras, números e espaços' )


class FornSelect( forms.Form ):

    forn_id = forms.CharField( 
        widget = forms.TextInput( attrs = {
            'style' : "display : none"
        })
    )
