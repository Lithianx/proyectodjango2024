$(document).ready(function () {

    
    $.getJSON('https://mindicador.cl/api', function () {

       /*$("#dolar").text(data.dolar.valor);*/

    }).fail(function () {
        console.log('Error al consumir la API!');
        $("#dolar").text('Error al consumir la API!');
    }).done(function(data)
    {
       
        $(".spinner").hide();
        $("#dolar").text("CLP$" + data.dolar.valor);
        
    });
});