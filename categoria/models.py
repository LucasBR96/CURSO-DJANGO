from django.db import models

# Create your models here.

class Categoria( models.Model ):

    nome = models.CharField( max_length = 70 , db_index = True, unique = True)

    # ------------------------------------------------------------------------
    # para indexação usada por buscadores como google.
    slug = models.SlugField( max_length = 70 )

    class Meta:

        #---------------------------------------------------------------------
        # mapeia as instâncias da classe categoria para entradas da tabela ca
        # tegoria.
        db_table = 'categoria'

        #---------------------------------------------------------------------
        # define por qual atributo as instâncias serão ordenadas
        ordering = ('nome',)

    def __str__(self):
        return self.nome
        
