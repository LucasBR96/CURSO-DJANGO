$( ".comprar" ).click( function(){

    this.blur();
    let botao = this;

    // ----------------------------------------------------
    // Acha o elemento html que anteced o botão de comprar
    // Nesse caso, form
    let form = $( botao ).prev();

    // -----------------------------------------------------
    // Achando o input que determina quantidade, e atribuindo
    // valor 1
    form.find( "input[ name = 'quantidade']").val( 1 );
    console.log( form );

    let url = form.attr( 'action' );
    let formData = form.serializeArray();
    console.log( formData );

    $.post( url , formData,
        function( resposta ){
            $(botao).fadeTo( 'fast' , 0.3 , function(){
                $(botao).hide();
                form.show();

                if( resposta.qtd === 1 ){
                    // $("#total-1").text( resposta.qtd + "item" + resposta.prec );
                    let s = " item -";
                }else if ( resposta.qtd > 1){
                    let s = " itens -";
                }$("#total-1").text( resposta.qtd + s + resposta.prec );

            })
        })
})

$(".mais").click( function(){

    this.blur();

    let input = $( this ).parent().prev();
    console.log( input );

    let num   = +input.val() + 1;
    console.log( num );
    if( num >= 100 ){
        return;
    }

    input.val( num );
    let form = $( this ).parent().parent().parent();

    let url = form.attr( 'action' );
    let formData = form.serializeArray();

    $.post( url , formData, function( resposta ){
            console.log( "O botão \"mais\" foi clicado" );

            if( resposta.qtd === 1 ){
                // $("#total-1").text( resposta.qtd + "item" + resposta.prec );
                let s = " item -";
            }else if ( resposta.qtd > 1){
                let s = " itens -";
            }$("#total-1").text( resposta.qtd + s + resposta.prec );
            })

} )

$(".menos").click( function(){

    this.blur();

    let input = $( this ).parent().next();
    console.log( input );

    let num   = +input.val() - 1;
    console.log( num );
    if( num < 0 ){
        return;
    }

    input.val( num );
    let form = $( this ).parent().parent().parent();

    let url = form.attr( 'action' );
    let formData = form.serializeArray();

    $.post( url , formData, function( resposta ){
            console.log( "O botão \"menos\" foi clicado" );

            if( resposta.qtd === 1 ){
                // $("#total-1").text( resposta.qtd + "item" + resposta.prec );
                let s = " item -";
            }else if ( resposta.qtd > 1){
                let s = " itens -";
            }$("#total-1").text( resposta.qtd + s + resposta.prec );
            })

} )
