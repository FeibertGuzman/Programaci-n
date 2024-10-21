// Seleccionar elementos del DOM
const numero1Input = document.getElementById('numero1');
const numero2Input = document.getElementById('numero2');
const numero3Input = document.getElementById('numero3');
const resultadoInput = document.getElementById('resultado');
const calcularBtn = document.querySelector('.btn_calcular');

// Función para multiplicar los tres números
function multiplicarTresNumeros(event) {
    // Evitar que la página se recargue
    event.preventDefault();

    // Convertir los valores de los inputs a números
    const num1 = parseFloat(numero1Input.value);
    const num2 = parseFloat(numero2Input.value);
    const num3 = parseFloat(numero3Input.value);

    // Verificar que los inputs no estén vacíos
    if (isNaN(num1) || isNaN(num2) || isNaN(num3)) {
        Swal.fire({
            icon: 'error',
            title: '¡Ups!',
            showConfirmButton: false,
            backdrop: `
                rgba(15, 53, 75,0.60)
                left top
                no-repeat
                    `,
            html: ' <h2>Para obtener un resultado debes diligenciar todos los campos.</h2>',
            showCancelButton: false,
            showConfirmButton: true,
            confirmButtonColor: '#1E2B63',
            allowOutsideClick: false
        });
        return;  // Detener la ejecución si los campos no son válidos
    }

    // Realizar la multiplicación
    const resultado = num1 * num2 * num3;

    // Mostrar el resultado en el campo de texto
    Swal.fire({
        icon: 'success',
        title: 'El resultado de la multiplicación es:',
        showConfirmButton: false,
        backdrop: `
            rgba(15, 53, 75,0.60)
            left top
            no-repeat
                `,
        html: 'La operación ingresada fue: "' + num1 + ' x ' + num2 + ' x ' + num3 + '" <br> <h2> RESTULADO= <b>' + resultado + '</b></h2>',
        showCancelButton: false,
        showConfirmButton: true,
        confirmButtonColor: '#1E2B63',
        allowOutsideClick: false
    });

    // También puedes mostrar el resultado en el input de resultado si lo deseas
    resultadoInput.value = resultado;
}

// Agregar evento al botón para ejecutar la función
calcularBtn.addEventListener('click', multiplicarTresNumeros);
