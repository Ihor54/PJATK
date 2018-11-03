'use strict';

function isPrime(num){
    for(let i = 2; i < num; i++)
        if (num % i === 0) return false;
    return num === 0 || num === 1 ? false : true;
}

let n = 13;

console.log(isPrime(n));