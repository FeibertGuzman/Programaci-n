function sumar() {
    realizarOperacion("suma");
}

function restar() {
    realizarOperacion("resta");
}

function multiplicar() {
    realizarOperacion("multiplicacion");
}

function dividir() {
    realizarOperacion("division");
}

function realizarOperacion(operacion) {
    var num1 = document.getElementById("numero1").value;
    var num2 = document.getElementById("numero2").value;

    num1 = parseFloat(num1);
    num2 = parseFloat(num2);
    var resultado;

    switch (operacion) {
        case "suma":
            resultado = num1 + num2;
            break;
        case "resta":
            resultado = num1 - num2;
            break;
        case "multiplicacion":
            resultado = num1 * num2;
            break;
        case "division":
            if (num2 !== 0) {
                resultado = num1 / num2;
            } else {
                document.getElementById("resultado").innerText = "Error: No se puede dividir por cero.";
                return;
            }
            break;
        default:
            document.getElementById("resultado").innerText = "Operación no válida.";
            return;
    }

    document.getElementById("resultado").innerText = resultado;
}
