
$(function () {

    $("#formulario").validate ({
        rules: {
            nombreObra: {
                required: true
            },
            desc: {
                required: true,
                minlength: 5
            }
        },
        messages: {
            nombreObra: {
                required: "Debe ingresar el nombre de la obra"
            },
            desc: {
                required: "Debe ingresar una descripcion",
                minlength: "Ingrese una descripcion valida"
            }
        }
    });
});