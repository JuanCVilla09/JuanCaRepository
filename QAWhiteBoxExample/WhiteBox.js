// Pruebas de caja blanca.
function sumar(num1, num2)
{
    if (typeof num1 !== 'number' || typeof num2 !== 'number') 
        {
            return "Error: Ambos parámetros deben ser números";
        }
    return num1 + num2;
}

var resultado = sumar(10,20)
console.log ("El resultado de la suma es: " + resultado);