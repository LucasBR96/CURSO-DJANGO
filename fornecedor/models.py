from django.db import models
from collections import namedtuple

visual_tuple = namedtuple( 'visual_tuple', ['id' , 'Nome' , 'Telefone' , 'CNPJ' , 'Endereco'] )
trow_tuple   = namedtuple( 'card_tuple', ['id' , 'Nome' , 'CNPJ', 'Telefone'] )

# Create your models here.
class Fornecedor( models.Model ):
    
    Nome     = models.CharField( max_length = 100 , unique = True , blank = False )
    Endereco = models.CharField( max_length = 100 , unique = False , blank = False )
    Telefone = models.CharField( max_length = 25 , unique = True , blank = False )
    CNPJ     = models.CharField( max_length = 30 , unique = True , blank = False )

    class Meta:
        db_table = 'fornecedor'

    
    def __str__( self ):
        return self.Nome + " " + self.CNPJ
    
    def formata_telefone( self ):

        s  = self.Telefone
        s1 = s[ : 2 ]
        s2 = s[ 2 : 7 ]
        s3 = s[ 7 :  ]

        return "({}) {} {}".format( s1 , s2 , s3 )
    
    def formata_CNPJ( self ):

        s  = self.CNPJ

        s1 = s[ :2 ]
        s2 = s[ 2:5 ]
        s3 = s[ 5:8 ]
        s4 = s[ 8:12 ]
        s5 = s[ 12: ]

        return "{}.{}.{}/{}-{}".format( s1 , s2 , s3 , s4 , s5 )
        
    def get_visual_tuple( self ):

        return visual_tuple(
            id = self.id,
            Nome = self.Nome,
            Telefone = self.formata_telefone(),
            CNPJ = self.formata_CNPJ(),
            Endereco = self.Endereco,
        )
    
    def get_trow_tuple( self ):

        return trow_tuple(
            id = self.id,
            Nome = self.Nome,
            CNPJ = self.formata_CNPJ(),
            Telefone = self.formata_telefone()
        )