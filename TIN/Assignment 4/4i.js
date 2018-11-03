'use strict';

Array.prototype.addMultiple = function(el, num){
    for(let i = 0; i < num; i++)
        this.push(el);
}

function countCoins(num, arr){
    let result = [],
        len = arr.length;

    for(let i = 0; i < len; i++){
        let numOfOccurs = Math.floor(num/arr[i]);
        num -= arr[i] * numOfOccurs;
        result.addMultiple(arr[i], numOfOccurs);
    }

    return result;
}

console.log(countCoins(46, [25, 10, 5, 2, 1]));