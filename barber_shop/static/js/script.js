

function mostrarSelecion(){
    val = document.querySelector('#id__categoria').value
    val_num = Number(val)
    console.log(val_num);
    buscapPorCategoria(val_num)

};

function buscapPorCategoria(id){
    url = getURL(window.location.href)+ id
    location.replace(url)
}

function getURL(url) { 
    let arr = url.split("/");
    ruta = `${arr[0]}//${arr[2]}/categoria/`
    return ruta
    }     

function eliminarProducto(){
    botonera = document.querySelector('#botonera');
    botonera.hidden = false

}

function ocultarBotoner(){
    botonera = document.querySelector('#botonera');
    botonera.hidden = true
}