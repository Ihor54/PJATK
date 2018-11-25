'use strict';
function celsiusToFahrenheit(temp) {
    return temp * 1.8 + 32;
}

function fahrenheitToCelsius(temp) {
    return (temp -32) / 1.8;
}

function handle(){
    let temp = document.getElementById('temp').value;
    let result = document.getElementById('result');
    let convertUnit = document.getElementById('units').value;
    let resultText = convertUnit === 'celsius' ? celsiusToFahrenheit(temp) : fahrenheitToCelsius(temp);
    result.textContent=resultText.toFixed(2);
    
}
