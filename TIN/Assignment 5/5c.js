'use strict';

let studentProto = {
    courses: ['WSI', 'TIN', 'RBD', 'MAD', 'BYT']
}

function newStudent(proto, firstName, lastName, id){
    let obj = Object.create(proto);
    obj.firstName = firstName;
    obj.lastName = lastName;
    obj.id = id;
    return obj;
}

let s1 = newStudent(studentProto, 'Bob', 'Peterson', '12543');

console.log(s1.courses);
