from django import forms

class QuantidadeForm( forms.Form ):

    #------------------------------------------------------------
    # forms.HiddenInput torna produto_id invisivel para o usuário
    produto_id = forms.CharField( widget = forms.HiddenInput() ,
    max_length = 4 , required = True )


    quantidade = forms.IntegerField( 
        min_value = 0,
        max_value = 99,
        widget = forms.TextInput( attrs = { 'class' : 'form-control btn-secondary bg-secondary quantidade' ,
                                            'width': '70px',
                                            'readonly': 'readonly'} ),
        required  = True )

