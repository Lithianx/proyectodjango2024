$(document).ready(function() {
    $("#addUserForm").validate({
    rules: {
        Nombre: {
        required: true,
        minlength: 2
        },
        Apellido: {
        required: true,
        minlength: 2
        },
        Email: {
        required: true,
        email: true
        },
        Numero: {
        required: true,
        digits: true
        }
    },
    messages: {
        Nombre: {
        required: "Por favor ingresa un nombre",
        minlength: "El nombre debe tener al menos 2 caracteres"
        },
        Apellido: {
        required: "Por favor ingresa un apellido",
        minlength: "El apellido debe tener al menos 2 caracteres"
        },
        Email: {
        required: "Por favor ingresa un email",
        email: "Por favor ingresa un email válido"
        },
        Numero: {
        required: "Por favor ingresa un número de teléfono",
        digits: "Por favor ingresa solo dígitos"
        }
    },
    submitHandler: function(form) {
        form.submit();
    }
    });
});

$(document).ready(function() {
    $("#editUserFormperfil").validate({
    rules: {
        nombreP: {
        required: true,
        minlength: 2
        },
        correo: {
        required: true,
        email: true
        },
        direccion: {
        required: true,
        minlength: 5
        }
    },
    messages: {
        nombreP: {
        required: "Por favor ingresa un nombre",
        minlength: "El nombre debe tener al menos 2 caracteres"
        },
        correo: {
        required: "Por favor ingresa un correo",
        email: "Por favor ingresa un correo válido"
        },
        direccion: {
        required: "Por favor ingresa una dirección",
        minlength: "La dirección debe tener al menos 5 caracteres"
        }
    },
    submitHandler: function(form) {
        form.submit();
    }
    });
});


  // Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
    .forEach(function (form) {
        form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
}

        form.classList.add('was-validated')
        }, false)
    })
})()

$(document).ready(function() {
    $("#editUserForm").validate({
    rules: {
        Nombre: {
        required: true,
        minlength: 2
        },
        Apellido: {
        required: true,
        minlength: 2
        },
        Email: {
        required: true,
        email: true
        },
        tipoCurso: {
        required: true
        },
        Numero: {
        required: true,
        digits: true
        }
    },
    messages: {
        Nombre: {
        required: "Por favor ingresa un nombre",
        minlength: "El nombre debe tener al menos 2 caracteres"
        },
        Apellido: {
        required: "Por favor ingresa un apellido",
        minlength: "El apellido debe tener al menos 2 caracteres"
        },
        Email: {
        required: "Por favor ingresa un correo",
        email: "Por favor ingresa un correo válido"
        },
        tipoCurso: {
        required: "Por favor selecciona un tipo de curso"
        },
        Numero: {
        required: "Por favor ingresa un número de teléfono",
        digits: "Por favor ingresa solo números"
        }
    },
    submitHandler: function(form) {
        form.submit();
    }
    });
});

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }

          form.classList.add('was-validated')
        }, false)
      })
  })()

  function confirmarBloquear(userId) {
    $('#confirmarBloquearModal').modal('show');

    // Al hacer clic en "Sí", realizar la acción de bloquear
    $('#confirmarBloquearBtn').click(function() {
        // Aquí colocarías la lógica para bloquear el usuario con el userId proporcionado
        // Por ejemplo, enviar una solicitud al servidor para bloquear el usuario con ese userId
        // Después de completar la acción, cierra el modal de confirmación
        $('#confirmarBloquearModal').modal('hide');
        console.log("Bloquear usuario con ID:", userId);
    });
}


function confirmarEliminar(userId) {
    $('#confirmarEliminarModal').modal('show');

    // Al hacer clic en "Sí", realizar la acción de eliminar
    $('#confirmarEliminarBtn').click(function() {
        // Aquí colocarías la lógica para eliminar el usuario con el userId proporcionado
        // Por ejemplo, enviar una solicitud al servidor para eliminar el usuario con ese userId
        // Después de completar la acción, cierra el modal de confirmación
        $('#confirmarEliminarModal').modal('hide');
        console.log("Eliminar usuario con ID:", userId);
    });
}
//VALIDACION AGREGAR USUARIO
$(document).ready(function() {
    $("#agregarUsuarioModal form").validate({
        rules: {
            ID: {
                required: true,
                digits: true
            },
            Nombre: {
                required: true,
                minlength: 2
            },
            Apellido: {
                required: true,
                minlength: 2
            },
            Email: {
                required: true,
                email: true
            },
            tipoCurso: {
                required: true
            },
            Numero: {
                required: true,
                digits: true
            }
        },
        messages: {
            ID: {
                required: "Por favor ingresa un ID",
                digits: "Por favor ingresa solo números"
            },
            Nombre: {
                required: "Por favor ingresa un nombre",
                minlength: "El nombre debe tener al menos 2 caracteres"
            },
            Apellido: {
                required: "Por favor ingresa un apellido",
                minlength: "El apellido debe tener al menos 2 caracteres"
            },
            Email: {
                required: "Por favor ingresa un correo",
                email: "Por favor ingresa un correo válido"
            },
            tipoCurso: {
                required: "Por favor selecciona un tipo de curso"
            },
            Numero: {
                required: "Por favor ingresa un número de teléfono",
                digits: "Por favor ingresa solo números"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });
});
//VALIDACION EDITAR USUARIO
$(document).ready(function() {
    $("#editarUsuarioModal form").validate({
        rules: {
            ID: {
                required: true,
                digits: true
            },
            Nombre: {
                required: true,
                minlength: 2
            },
            Apellido: {
                required: true,
                minlength: 2
            },
            Email: {
                required: true,
                email: true
            },
            tipoCurso: {
                required: true
            },
            Numero: {
                required: true,
                digits: true
            }
        },
        messages: {
            ID: {
                required: "Por favor ingresa un ID",
                digits: "Por favor ingresa solo números"
            },
            Nombre: {
                required: "Por favor ingresa un nombre",
                minlength: "El nombre debe tener al menos 2 caracteres"
            },
            Apellido: {
                required: "Por favor ingresa un apellido",
                minlength: "El apellido debe tener al menos 2 caracteres"
            },
            Email: {
                required: "Por favor ingresa un correo",
                email: "Por favor ingresa un correo válido"
            },
            tipoCurso: {
                required: "Por favor selecciona un tipo de curso"
            },
            Numero: {
                required: "Por favor ingresa un número de teléfono",
                digits: "Por favor ingresa solo números"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });
});
//VALDIACION FECHA VENCIMIENTO
$(document).ready(function() {
    $('#cc-expiration').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^0-9/]/g, '');
        if (value.length > 5) {
            value = value.substr(0, 5);
        }
        if (value.length === 3 && value[2] !== '/') {
            value = value.substr(0, 2) + '/' + value.substr(2);
        }
        $(this).val(value);
    });
});
//VALIDACION NOMBRE TARJETA
$(document).ready(function() {
    $('#cc-name').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION NOMBRE
$(document).ready(function() {
    $('#firstName').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION APELLIDO
$(document).ready(function() {
    $('#lastName').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION NUMERO TARJETA
$(document).ready(function() {
    $('#cc-number').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^0-9]/g, '');

        if (value.length > 16) {
            value = value.substr(0, 16);
        }
        value = value.replace(/(\d{4})/g, '$1-');
        value = value.replace(/-$/, '');
        $(this).val(value);
    });
});
//VALIDACION CVV
$(document).ready(function() {
    $('#cc-cvv').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^0-9]/g, '');        
        if (value.length > 3) {
            value = value.substr(0, 3);
        }
        $(this).val(value);
    });
});
//VALIDACION RUT
$(document).ready(function() {
    $('#rut').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^0-9kK]/g, '');
        value = value.replace(/(\d{1,2})(\d{3})(\d{3})([0-9kK]{1})/, '$1.$2.$3-$4');
        if (value.length > 12) {
            value = value.substr(0, 12);
        }
        $(this).val(value);
    });
});
//VALIDACION PROMO
$(document).ready(function() {
    $('#promo').on('input', function() {
        var value = $(this).val();
        // Permitir solo letras y números, sin espacios
        value = value.replace(/[^a-zA-Z0-9]/g, '');
        //el valor se convierte en mayúsculas
        value = value.toUpperCase();
        $(this).val(value);
    });
});

  
  //VALIDACION NOMBRE PERFIL USUARIO
$(document).ready(function() {
    $('#nombreP').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION NOMBRE AGREGAR USUARIO
$(document).ready(function() {
    $('#NombreA').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION APELLIDO AGREGAR USUARIO
$(document).ready(function() {
    $('#ApellidoA').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION NOMBRE EDITAR USUARIO
$(document).ready(function() {
    $('#NombreB').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});
//VALIDACION APELLIDO EDITAR USUARIO
$(document).ready(function() {
    $('#ApellidoB').on('input', function() {
        var value = $(this).val();
        value = value.replace(/[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]/g, '');
        value = value.replace(/\s{2,}/g, ' ');
        $(this).val(value);
    });
});