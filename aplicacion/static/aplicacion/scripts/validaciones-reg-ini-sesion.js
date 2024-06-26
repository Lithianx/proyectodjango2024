//validacion para el apartado de registro

$(document).ready(function() {
    // Función para validar los campos y coordinar la animación del color del campo
    function validarCampos() {
        var nombre = $('#nombre').val();
        var email = $('#email').val();
        var contrasena = $('#contrasena').val();

        // Validar el nombre (mínimo 3 caracteres y solo letras)
        if (/^[a-zA-Z]{3,}$/.test(nombre)) {
            $('#nombre').removeClass('is-invalid').addClass('is-valid');
        } else {
            $('#nombre').removeClass('is-valid').addClass('is-invalid');
        }

        // Validar el email (formato de email válido)
        if (/\S+@\S+\.\S+/.test(email)) {
            $('#email').removeClass('is-invalid').addClass('is-valid');
        } else {
            $('#email').removeClass('is-valid').addClass('is-invalid');
        }

        // Validar la contraseña (mínimo 6 caracteres)
        if (/^.{6,}$/.test(contrasena)) {
            $('#contrasena').removeClass('is-invalid').addClass('is-valid');
        } else {
            $('#contrasena').removeClass('is-valid').addClass('is-invalid');
        }

        // Verificar si todos los campos están cubiertos
        if ($('#nombre').hasClass('is-valid') && $('#email').hasClass('is-valid') && $('#contrasena').hasClass('is-valid')) {
            // Habilitar el botón de registro
            $('#b-registro').prop('disabled', false);
        } else {
            // Deshabilitar el botón de registro
            $('#b-registro').prop('disabled', true);
        }
    }

    // Validaciones cuando se completa la entrada en los campos
    $('#nombre, #email, #contrasena').on('input', function() {
        validarCampos();
    });

    // Validaciones cuando se envía el formulario
    $('#registroForm').submit(function(event) {
        event.preventDefault(); // Prevenir la presentación del formulario por defecto

        var nombre = $('#nombre').val();
        var email = $('#email').val();
        var contrasena = $('#contrasena').val();

        // Validar el email (formato de email válido)
        if (!/\S+@\S+\.\S+/.test(email)) {
            $('#email').removeClass('is-valid').addClass('is-invalid');
            return;
        }

        // Si todas las validaciones pasan, podría enviar el formulario
        alert("¡Formulario enviado con éxito!");
        
    });

    // Inicialmente, deshabilitar el botón de registro
    $('#b-registro').prop('disabled', true);
});










// validacion para el apartado de inicio de sesion


$(document).ready(function() {
    // Función para validar los campos
    function validarCampos() {
        var nombre = $('#uname').val(); // Obtener el valor del campo de nombre
        var contrasena = $('#pwd').val(); // Obtener el valor del campo de contraseña

        // Validar el nombre (mínimo 3 caracteres y solo letras)
        if (/^[a-zA-Z]{3,}$/.test(nombre)) {
            $('#uname').removeClass('is-invalid').addClass('is-valid');
        } else {
            $('#uname').removeClass('is-valid').addClass('is-invalid');
        }

        // Validar la contraseña (mínimo 6 caracteres alfanuméricos)
        if (/^[a-zA-Z0-9]{6,}$/.test(contrasena)) {
            $('#pwd').removeClass('is-invalid').addClass('is-valid');
        } else {
            $('#pwd').removeClass('is-valid').addClass('is-invalid');
        }

        // Verificar si todos los campos están cubiertos
        if ($('#uname').hasClass('is-valid') && $('#pwd').hasClass('is-valid')) {
            // Habilitar el botón de inicio de sesión
            $('#registroForm button[type="submit"]').prop('disabled', false);
        } else {
            // Deshabilitar el botón de inicio de sesión
            $('#registroForm button[type="submit"]').prop('disabled', true);
        }
    }

    // Validaciones cuando se completa la entrada en los campos
    $('#uname, #pwd').on('input', function() {
        validarCampos();
    });

    // Validaciones cuando se envía el formulario
    $('#registroForm').submit(function(event) {
        event.preventDefault(); // Prevenir la presentación del formulario por defecto

        // Aquí podrías agregar el código para enviar el formulario
        window.location.href = 'perfil.html';
    });

    // Inicialmente, deshabilitar el botón de inicio de sesión
    $('#registroForm button[type="submit"]').prop('disabled', true);
});












