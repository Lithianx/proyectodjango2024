$(document).ready(function() {
    $('.precio-input').on('input', function() {
        var precio = parseInt($(this).val());
        if (precio < 0 || precio > 9999999) {
            $(this).addClass('is-invalid');
        } else {
            $(this).removeClass('is-invalid');
        }
    });
});