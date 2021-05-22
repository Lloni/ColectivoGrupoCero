var validaNombre = function() {
    var nom = document.getElementById("idnombre").value;
    if (nom.length > 0) {
        return true;
    } else {
        return false;
    }
}

var validarCorreo = function() {
    var correo = document.getElementById("idcorreo").value;
    if (correo.length > 0) {
        return true;
    } else {
        return false;
    }
}

var validarContraseña = function() {
    var contra = document.getElementById("idcontraseña").value;
    if (contra.length > 6) {
        return true;
    } else {
        return false;
    }
}


var validarFunciones = function() {
    if (validaNombre() == true) {} else {
        envio = "El campo nombre debe ser ingresado";
        return envio;
    }
    if (validarCorreo() == true) {} else {
        envio = "Debe ingresar un correo (Ejemplo: Correo123@gmail.com)"
        return envio;
    }
    if (validarContraseña() == true) {} else {
        envio = "El campo contraseña debe contener como mínimo 7 caracteres";
        return envio;
    }
    if (validaNombre() == true && validarCorreo() == true && validarContraseña() == true) {
        envio = "Ingreso exitoso, Bienvenido!";
        return envio;
    }
}