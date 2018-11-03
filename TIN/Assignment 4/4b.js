"use strict";

function fib(index){
    return index < 2 ? index : fib(index - 1) + fib(index - 2);
}

let n = 6;

console.log(fib(n));
