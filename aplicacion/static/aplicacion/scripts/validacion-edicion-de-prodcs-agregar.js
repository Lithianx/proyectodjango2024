$(document).ready(function(){
    // Validación del campo "curso"
    $('#precio').on('input', function() {
        var precio = $(this).val();
        if (!/^\d{1,9}$/.test(precio) || precio < 1 || precio > 999999999) {
            $(this).addClass('is-invalid');
        } else {
            $(this).removeClass('is-invalid');
        }
    });
    

    // Validación del campo "cupos"
    $('#cupos').on('input', function() {
        var cupos = $(this).val();
        if (cupos < 0) {
            $(this).addClass('is-invalid');
        } else {
            $(this).removeClass('is-invalid');
        }
    });

    // Validación del campo "tipoCurso"
    $('#tipoCurso').on('input', function() {
        var tipoCurso = $(this).val();
        if (!/^[a-e1-5]+$/.test(tipoCurso)) {
            $(this).addClass('is-invalid');
        } else {
            $(this).removeClass('is-invalid');
        }
    });

    // Evitar que se envíe el formulario si hay campos inválidos
    $('.form-control').on('input', function() {
        var formularioValido = true;
        $('.form-control').each(function() {
            if ($(this).hasClass('is-invalid')) {
                formularioValido = false;
                return false; // Termina el bucle each
            }
        });
        if (formularioValido) {
            $('button[type="submit"]').prop('disabled', false);
        } else {
            $('button[type="submit"]').prop('disabled', true);
        }
    });
});