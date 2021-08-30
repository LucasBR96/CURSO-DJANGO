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
            })
        })
})