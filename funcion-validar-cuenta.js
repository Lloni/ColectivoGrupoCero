var validaNombre = function() {
    var nom = document.getElementById("idnombre").value;
    if (nom.length > 3) {
        return true;
    } else {
        return false;
    }
}

var validarEmail = function() {
    var contra = document.getElementById("idcorreo").value;
    re = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
    if (!re.exec(contra)) {
        return false;
    } else {
        return true
    };
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
    if (validarEmail() == true) {} else {
        envio = "Debe ingresar un correo (Ejemplo: Correo123@gmail.com)"
        return envio;
    }
    if (validarContraseña() == true) {} else {
        envio = "El campo contraseña debe contener como mínimo 7 caracteres";
        return envio;
    }
    if (validaNombre() == true && validarEmail() == true && validarContraseña() == true) {
        envio = "Ingreso exitoso, Bienvenido!";
        return envio;
    }
}