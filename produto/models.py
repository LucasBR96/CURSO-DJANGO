from categoria.models import Categoria
from django.db import models

# Create your models here.
class Produto( models.Model):

    #-------------------------------------------------------------------------
    # Cria a chave estrangeira. No caso desse tutorial a releção Produto/Categoria
    # é de muitos para um
    categoria = models.ForeignKey( Categoria , on_delete = models.DO_NOTHING )

    #-------------------------------------------------------------------------
    # o nome do produto ( alface , batata , beterraba e por aí vai )
    nome = models.CharField( max_length = 100 , db_index = True, unique = True)

    #-------------------------------------------------------------------------
    # o mesmo slug de Categoria
    slug = models.SlugField( max_length = 100 )

    # -------------------------------------------------------------------------
    # string contendo o nome do arquivo que contém a imagem, não a imagem em si
    img = models.CharField( max_length = 200 , blank = True )

    #-------------------------------------------------------------------------
    # quantidade de produtos em estoque
    qdt_est = models.IntegerField( default = 0 )

    #------------------------------------------------------------------------
    # max_digits e decimal_places iguais a 5 e 2, respectivamente, significam
    # que o preço max é de 999.99
    preco   = models.DecimalField( default = 0. , max_digits = 5 , decimal_places = 2 )

    #-------------------------------------------------------------------------
    # um produto pode ter mais de zero unidades em estoque e mesmo assim, por
    # qualquer motivo, estar indisponível
    disponivel = models.BooleanField( default = False)

    class Meta:
        db_table = 'produto'

    def __str__( self ):
        return self.nome