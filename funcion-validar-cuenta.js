var validaNombre = function(){
    var nom = document.getElementById("idnombre").value;
    if(nom.length>0){
        return true;
    }else{
        return false;
    }
}

var validarCorreo = function(){
    var correo = document.getElementById("idcorreo").value;
    if(correo.length>0){
        return true;
    }else{
        return false;
    }
}

var validarContraseña = function(){
    var contra = document.getElementById("idcontraseña").value;
    if(contra.length>0){
        return true;
    }else{
        return false;
    }
}


var validarFunciones =function(){
    if(validaNombre()==true){
    }else{
        envio="El campo nombre debe ser ingresado";
        return envio;
    }
    if(validarCorreo()==true){
    }else{
        envio="Debe ingresar un correo (Ejemplo: Correo123@gmail.com)"
        return envio;
    }
    if(validarContraseña()==true){
    }else{
        envio="El campo contraseña debe contener como mínimo 7 caracteres";
        return envio;
    }
    if(validaNombre()==true&&validarCorreo()==true&&validarContraseña()==true){
        envio="CUENTA CREADA CORRECTAMENTE";
        window.location.href = "publicacion.html";
        return envio;
    }
}


// var validarFunciones =function(){
//     if !(validaNombre()==true){
//         envio="El campo nombre debe ser ingresado";
//         return false;
        
//     } else if !(validarCorreo()==true){
//         envio="Debe ingresar un correo (Ejemplo: Correo123@gmail.com)"
//         return false;
//     }
//     else if !(validarContraseña()==true){
//         envio="El campo contraseña debe contener como mínimo 7 caracteres";
//         return false;
//     } else if (validaNombre()==true&&validarCorreo()==true&&validarContraseña()==true){
//         envio="CUENTA CREADA CORRECTAMENTE";
//         return false;
//     } else {
//         window.location.href = "publicacion.html";
//     }

// }
