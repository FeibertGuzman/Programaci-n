console.log("Un saludo desde la consola");

function multiplica(x, y, z) {
    console.log("La multiplicación es:", x * y * z);
}
multiplica(2, 5, 2);

// Función para sumar dos números
function sumaNumeros() {
    let numero1 = parseFloat(document.getElementById("numero1").value);
    let numero2 = parseFloat(document.getElementById("numero2").value);

    if (isNaN(numero1) || isNaN(numero2)) {
        alert("Por favor, ingresa nUmeros válidos.");
    } else {
        let resultado = numero1 + numero2;
        document.getElementById("resultado").innerText = "La suma es: " + resultado;
    }
}
