'use strict';

function secondLL(arr) {
    let s = Array.from(new Set(arr)).sort((a, b) => { return a - b; });
    return [s[1], s[s.length - 2]];
}

let arr = [1, 240, 3, 0, 3, 32, 1, 3, 4, 2, 1, 4];

console.log(secondLL(arr));