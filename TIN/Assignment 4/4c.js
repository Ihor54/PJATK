"use strict";

function isPalindrome(val){
    let len = val.length;
    for(let i = 0; i < len / 2; i++){
        if (val[i] !== val[len - i - 1])
            return false;
    }
    return true;
}

function isPalindrome2(val){
    return val === val.split('').reverse().join('');
}

let val = 'aaabbbaaa';

console.log(isPalindrome(val));

console.log(isPalindrome2(val));