let btnCarrito = document.getElementById("btnCarrito");

btnCarrito.addEventListener('click',function(){
    array_productos = [
        {
            sku:1,
            nombre:"Steam Random Key x5",
            precio:4000,
            cantidad:1
        },
        {
            sku:2,
            nombre:"Steam Gold Random Key x3",
            precio:10000,
            cantidad:2
        },
        {
            sku:3,
            nombre:"Steam Random Key x30",
            precio:15000,
            cantidad:1
        }
    ]
    
    
        let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        fetch('/carrito',{
            
        method:'POST',
        headers:{
            'Content-type': 'application/json',
            'X-CSRFToken':token,
        },
        body:JSON.stringify(array_productos)
        })
        console.log("11111111111111", array_productos); 


})