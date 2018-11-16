'use strict';

class Person{
    constructor(firstName, lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }
    get fullName() {
        return this.firstName + ' ' + this.lastName;
    }

    set fullName(name){
        let words = name.split(' ');
        this.firstName = words[0] || '';
        this.lastName = words[1] || '';
    }
}


class Student extends Person{
    constructor(firstName, lastName, id, grades){
        super(firstName, lastName);
        this.id = id;
        this.grades = grades;
    }

    get avgGrade() {
        return this.grades.reduce((x, y) => x + y) / this.grades.length;
    }
}

let st1 = new Student('Bob', 'Peterson', '12543', [4, 3, 6, 3]);

console.log(st1.avgGrade);
console.log(st1.fullName);

st1.fullName = 'John Brown';
console.log(st1.fullName);
