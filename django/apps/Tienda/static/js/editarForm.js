const formulario = document.getElementById("formProductoAgregar")

formulario.addEventListener('submit',function(evento){
    evento.preventDefault();

    if (document.getElementById("txtSku").value.length == 0) {
        alert("Debe ingresar el codigo del producto.");
    }else{
        this.submit();
    }
})