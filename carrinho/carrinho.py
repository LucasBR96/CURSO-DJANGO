from projeto import settings
from produto.models import Produto

class Carrinho( object ):

    def __init__ ( self , request ):

        self.session = request.session
        self.carrinho = self.session.get( settings.CARRINHO_SESSION_ID )

        if self.carrinho is None:
            self.carrinho = self.session[ settings.CARRINHO_SESSION_ID ] = {}
        
    def atualizar( self , id , qtd ):

        produto = Produto.objects.get( id = id )
        if not id in self.carrinho:

            d = dict()
            d[ 'id' ] = str( id )
            d[ 'preco' ] = str( produto.preco )
            d[ 'quantidade'] = qtd
            d[ 'total' ] = str( qtd*produto.preco )

            self.carrinho[ id ] = d
        else:

            self.carrinho[ id ][ 'quantidade' ] = qtd
            self.carrinho[ id ][ 'total' ] = str( self.carrinho[id][ 'quantidade' ]*float( self.carrinho[id][ 'preco' ] ) )
        
        self.salvar()

    def salvar( self ):

        self.session.modified = True

    def remover( self , id ):

        if id in self.carrinho:
            del self.carrinho[ id ]
            self.salvar()

    def get_preco_total( self , id ):
        return self.carrinho[ id ][ 'total' ]

    def get_gasto_total( self ):

        soma = 0
        for id in self.carrinho :
            soma += float( self.get_preco_total( id ) )
        return str( soma )

    def get_quantidade( self , id ):
        return self.carrinho[ id ][ 'quantidade' ]
    
    def get_qtd_total( self ):
        return sum( self.get_quantidade( id ) for id in self.carrinho.keys() )

    def lista_de_produtos( self ):

        lst = []
        for id , prod in self.carrinho.items():

            produto = Produto.objects.get( id = id )
            prod_dict = prod.copy()
            prod_dict[ 'produto' ] = produto

            lst.append( prod_dict )

        return lst 

