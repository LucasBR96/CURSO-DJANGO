from carrinho.carrinho import Carrinho

def context_carrinho( request ):

    carrinho = Carrinho( request )
    qtd   = carrinho.get_qtd_total()
    gasto = carrinho.get_gasto_total()

    return{
        'qtd':qtd,
        'gasto':gasto
    }