'use strict';

let dog_obj = {
    legs: 4,
    ears: 2,
    tail: 1,
    eyes: 2,
    voice: function(){
        console.log('bark bark bark');
    },
    walk: function(){
        console.log('top top top');
    },
    dance: function(){
        console.log('shake shake shake');
    }
};

function list_props(obj){
    for(let prop in obj){
        console.log(prop + ' of type ' + typeof(prop));
    }
}

list_props(dog_obj);