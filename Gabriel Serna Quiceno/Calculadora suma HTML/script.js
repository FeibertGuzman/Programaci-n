// Función para realizar la suma
function sumar() {
    // Obtener los valores de los inputs
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);

    // Validar si los campos están vacíos
    if (isNaN(num1) || isNaN(num2)) {
        alert("Por favor ingrese ambos números.");
        return;
    }

    // Realizar la suma
    var resultado = num1 + num2;

    // Mostrar el resultado en el modal
    document.getElementById('resultado-texto').innerText = "El resultado es: " + resultado;
    abrirModal();
}

// Función para abrir el modal
function abrirModal() {
    var modal = document.getElementById('resultModal');
    modal.style.display = "block";
}

// Función para cerrar el modal
function cerrarModal() {
    var modal = document.getElementById('resultModal');
    modal.style.display = "none";
}

// Cerrar el modal si el usuario hace clic fuera del contenido
window.onclick = function(event) {
    var modal = document.getElementById('resultModal');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
