from projeto import settings
from produto.models import Produto

class Carrinho( object ):

    def __init__ ( self , request ):

        self.session = request.session
        self.carrinho = self.session.get( settings.CARRINHO_SESSION_ID )

        if self.carrinho is None:
            self.carrinho = self.session[ settings.CARRINHO_SESSION_ID ] = {}
        
    def atualizar( self , idt , qtd ):

        produto = Produto.objects.get( id = idt )
        if not idt in self.carrinho:

            d = dict()
            d[ 'id' ] = str( idt )
            d[ 'preco' ] = str( produto.preco )
            d[ 'quantidade'] = qtd
            d[ 'total' ] = str( qtd*produto.preco )

            self.carrinho[ idt ] = d
        else:

            self.carrinho[ idt ][ 'quantidade' ] = qtd
            self.carrinho[ idt ][ 'total' ] = str( self.carrinho[ idt ][ 'quantidade' ]*float( self.carrinho[idt][ 'preco' ] ) )
        
        self.salvar()

    def salvar( self ):

        self.session.modified = True

    def remover( self , idt ):

        if idt in self.carrinho:
            del self.carrinho[ idt ]
            self.salvar()

    def get_preco_total( self , idt ):
        return self.carrinho[ idt ][ 'total' ]

    def get_gasto_total( self ):

        soma = 0
        for idt in self.carrinho :
            soma += float( self.get_preco_total( idt ) )
        return str( soma )

    def get_quantidade( self , idt ):
        
        if not ( idt in self.carrinho ):
            self.atualizar( idt , 0 )
        return self.carrinho[ idt ][ 'quantidade' ]
    
    def get_qtd_total( self ):
        return sum( self.get_quantidade( idt ) for idt in self.carrinho.keys() )

    def lista_de_produtos( self ):

        lst = []
        for idt , prod in self.carrinho.items():

            produto = Produto.objects.get( id = idt )
            prod_dict = prod.copy()
            prod_dict[ 'produto' ] = produto

            lst.append( prod_dict )

        return lst 

