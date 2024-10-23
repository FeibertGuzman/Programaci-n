function sumar() {
    // Obtener los valores de los inputs
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    
    // Verificar si los valores son números
    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('resultado').innerText = 'Por favor, introduce números válidos.';
    } else {
        // Sumar los números y mostrar el resultado
        const suma = num1 + num2;
        document.getElementById('resultado').innerText = 'Resultado: ' + suma;
    }
}
