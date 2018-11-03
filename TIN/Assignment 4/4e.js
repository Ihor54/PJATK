'use strict';

function longest_word(str) {
    str = str.split(/[ ,.:;]/).sort((a, b) => {
        return b.length - a.length;
    });
    return str[0];
}

let sentence = 'Sort, items in an array alphabetically,  with. Array';

console.log(longest_word(sentence));



