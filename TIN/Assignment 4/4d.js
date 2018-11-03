'use strict';

function alphabetical(val){
    return val.split('').sort().join('');
}

let val = 'webmaster' ;

console.log(alphabetical(val));

