from django.db import models

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