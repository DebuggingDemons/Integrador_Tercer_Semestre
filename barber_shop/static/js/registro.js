const inputUsuario =  document.querySelector('#registro_usuario');
const inputPassword =  document.querySelector('#registro_password');
const inputVer_password =  document.querySelector('#registro_ver_password');
const inputEmail =  document.querySelector('#registro_email');
const inputNombre =  document.querySelector('#registro_nombre');
const inputApellido =  document.querySelector('#registro_apellido');

const boton_registro = document.querySelector('#btn_registrar');


inicio()
function inicio(){

    inputUsuario.focus()

    inputUsuario.addEventListener('blur',verificar);
    inputPassword.addEventListener('blur',verificar);
    inputVer_password.addEventListener('blur',verificar);
    inputVer_password.addEventListener('change',verificar_verPassword_coincide);
    inputEmail.addEventListener('blur',verificar);
    inputNombre.addEventListener('blur',verificar);
    inputApellido.addEventListener('blur',verificar);

}

function verificar(){

    let usuario = verificarUsuario()
        if (usuario) {
            let password = verificarPassword()
            if (password) {
                let ver_password = verificar_verPassword()
                if (ver_password){
                    let email = verificarEmail()
                    if (email){
                        let nombre = verificarNombre()
                        if (nombre) {
                            let apellido = verificarApellido()
                            if (apellido) {
                                let  pas_coincide= verificar_verPassword_coincide()
                                if (pas_coincide) {
                                    if (usuario && password &&  ver_password  && email  && nombre  && apellido && pas_coincide ) {
                                         if (password == ver_password) {
                                         boton_registro.disabled = false
                                         }
                                    }
                                }
                            }
                            
                        }

                    }

                }
            }
        }
    

    
}

function verificarUsuario(){

        let usuario =  inputUsuario.value
        const i_registro =  document.querySelector('#i_registro_usuario')
        if(usuario == ""){   
            i_registro.hidden= false
            setInterval(() => {
                i_registro.hidden = true
            }, 5000);
            return false
        }
        else{
            return true
        }
}

function verificarPassword(){
    let password =  inputPassword.value
    const i_registro =  document.querySelector('#i_registro_password')
    if(password == ""){
            i_registro.hidden= false
            setInterval(() => {
                i_registro.hidden= true
            }, 5000);
            return false
        }
    else{
        return true
    }
}


function verificar_verPassword(){
    let ver_password =  inputVer_password.value
    const i_registro =  document.querySelector('#i_verificacion_password_falta')
        if(ver_password.value == ""){
            i_registro.hidden= false
            setInterval(() => {
                i_registro.hidden= true
            }, 5000);
            return false
        }
        return true;
}


function verificarEmail(){
    let email = inputEmail.value
    const i_registro =  document.querySelector('#i_registro_email')
        if(email.value == ""){
            i_registro.hidden= false
            setInterval(() => {
                i_registro.hidden= true
            }, 5000);
            return false
        }else{
            return true
        }

}

function verificarNombre(){
    let nombre = inputNombre.value
    i_registro =  document.querySelector('#i_registro_nombre')
        if(nombre  == ""){
            i_registro.hidden= false
            setInterval(() => {
                i_registro.hidden= true
            }, 5000);
            return false
        }else{
            return true
        }
}

function verificarApellido(){
    let apellido = inputApellido.value
    i_registro =  document.querySelector('#i_registro_apellido')
    if(apellido == ""){
            i_registro.hidden= false
            setInterval(() => {
                i_registro.hidden= true
            }, 5000);
            return false
            }else{
                return true
            }
}

function verificar_verPassword_coincide(){
    let password = inputPassword.value
    let ver_password =  inputVer_password.value
    i_registro =  document.querySelector('#i_verificacion_password')
    if (password != ver_password) {
        i_registro.hidden= false
        setInterval(() => {
            i_registro.hidden= true
        }, 5000);
        return false
    }else{
        return true
    }

}
