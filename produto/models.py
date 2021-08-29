from django.db import models
from categoria.models import Categoria
from django.urls import reverse

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    descricao = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    imagem = models.CharField(max_length=50, blank=True)
    qtd_estoque = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data_cadastro = models.DateField()
    disponivel = models.BooleanField(default=False)

    class Meta:
        db_table='produto'

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        '''
        self.id = 11
        self.slug = laranja

        return carrinho/11/laranja
        '''
        return reverse( "carrinho:exibe_produto" , args = [ self.id , self.slug ] )

