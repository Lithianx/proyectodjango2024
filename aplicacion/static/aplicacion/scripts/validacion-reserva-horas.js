

    $(document).ready(function() {
        // Función para validar el nombre
        $('#nombreCompleto-horas').on('input', function() {
            var nombre = $(this).val();
            var valido = nombre.length >= 6 && /^[A-Za-z]+$/.test(nombre);
            $(this).toggleClass('is-invalid', !valido).toggleClass('is-valid', valido);
            validarBotonReserva();
        });
        
    
        // Función para validar el RUT chileno
        $('#id-rut-horas').on('input', function() {
            var rut = $(this).val();
            var valido = /^\d{1,9}-[\dkK]$/.test(rut);
            $(this).toggleClass('is-invalid', !valido).toggleClass('is-valid', valido);
            validarBotonReserva();
        });
    
        // Función para validar el email
        $('#email-horas').on('input', function() {
            var email = $(this).val();
            var valido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
            $(this).toggleClass('is-invalid', !valido).toggleClass('is-valid', valido);
            validarBotonReserva();
        });
    
        // Función para validar el teléfono
        $('#id-telefono-horas').on('input', function() {
            var telefono = $(this).val();
            var valido = /^9[0-9]{8}$/.test(telefono);
            $(this).toggleClass('is-invalid', !valido).toggleClass('is-valid', valido);
            validarBotonReserva();
        });
    
        // Función para validar el tipo de curso
        $('#tipoCurso').change(function() {
            var valido = $(this).val() !== '';
            $(this).toggleClass('is-invalid', !valido).toggleClass('is-valid', valido);
            validarBotonReserva();
        });
    
        // Función para validar la fecha de curso
        $('#fechaCurso').change(function() {
            var valido = $(this).val() !== '';
            $(this).toggleClass('is-invalid', !valido).toggleClass('is-valid', valido);
            validarBotonReserva();
        });
    
        // Función para validar y habilitar/deshabilitar el botón de reserva
        function validarBotonReserva() {
            var nombreValido = $('#nombreCompleto-horas').hasClass('is-valid');
            var rutValido = $('#id-rut-horas').hasClass('is-valid');
            var emailValido = $('#email-horas').hasClass('is-valid');
            var telefonoValido = $('#id-telefono-horas').hasClass('is-valid');
            var tipoCursoValido = $('#tipoCurso').hasClass('is-valid');
            var fechaCursoValida = $('#fechaCurso').hasClass('is-valid');
    
            var todosCamposValidos = nombreValido && rutValido && emailValido && telefonoValido && tipoCursoValido && fechaCursoValida;
    
            $('#reservarButton').prop('disabled', !todosCamposValidos);
        }
    });



    $(document).ready(function() {
        
    
        // Controlador de eventos click para el botón de reserva
        $('#reservarButton').on('click', function() {
            var nuevaPagina = 'interfaz_de_compra.html';
            window.location.href = nuevaPagina;
        });
    });
    

    
    
    