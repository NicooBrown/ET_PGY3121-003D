// Productos
$(document).ready(function() {
    var productList = [];
  
    // Validar el formulario y agregar producto
    $("#productForm").submit(function(event) {
      event.preventDefault();
  
      var productName = $("#productName").val();
      var productPrice = $("#productPrice").val();
  
      if (productName.trim() === '' || productPrice.trim() === '') {
        alert("Por favor, complete todos los campos");
        return;
      }
  
      var product = {
        name: productName,
        price: productPrice
      };
  
      productList.push(product);
  
      // Limpiar campos de entrada
      $("#productName").val("");
      $("#productPrice").val("");
  
      actualizarListaProductos();
    });
  
    // Actualizar la lista de productos
    function actualizarListaProductos() {
      $("#productList").empty();
  
      for (var i = 0; i < productList.length; i++) {
        var product = productList[i];
        var listItem = $("<li>").addClass("list-group-item").text(product.name + " - $" + product.price);
  
        var deleteButton = $("<button>")
          .addClass("btn btn-danger btn-sm float-end")
          .text("Eliminar")
          .data("index", i)
          .click(function() {
            var index = $(this).data("index");
            productList.splice(index, 1);
            actualizarListaProductos();
          });
  
        listItem.append(deleteButton);
        $("#productList").append(listItem);
      }
    }
  });
  


  // Reloj en tiempo real

  function startTime() {
    var today = new Date();
    var hr = today.getHours();
    var min = today.getMinutes();
    var sec = today.getSeconds();
    //Add a zero in front of numbers<10
    min = checkTime(min);
    sec = checkTime(sec);
    document.getElementById("clock").innerHTML = hr + " : " + min + " : " + sec;
    var time = setTimeout(function(){ startTime() }, 500);
}
function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}
  
// CONSUMIR API

$(document).ready(function() {
    $("#loadDataBtn").click(function() {
      $.ajax({
        url: "https://rickandmortyapi.com/api/character",
        method: "GET",
        dataType: "json",
        success: function(data) {
          mostrarPersonajes(data.results);
        },
        error: function(xhr, status, error) {
          console.log("Error al cargar los datos de la API:", error);
        }
      });
    });
  
    function mostrarPersonajes(personajes) {
      var apiDataElement = $("#apiData");
      apiDataElement.empty();
  
      for (var i = 0; i < personajes.length; i++) {
        var personaje = personajes[i];
        var item = $("<div>").text("Nombre: " + personaje.name + ", Especie: " + personaje.species);
        apiDataElement.append(item);
      }
    }
  });
  