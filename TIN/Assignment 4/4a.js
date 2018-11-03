"use strict";

let factorial = function fact(n) { return n < 2 ? 1 : n * fact(n - 1); };

let z = 3;

console.log(factorial(z));

function factorial_iter(n) {
    if (n < 2) return 1;
    for (let i = n; i > 1; i--) {
        n *= i - 1;
    }
    return n;
}

console.log(factorial_iter(z));