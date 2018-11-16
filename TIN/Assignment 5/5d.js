'use strict';

function Student(firstName, lastName, id, grades) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.id = id;
    this.grades = grades;

    Object.defineProperties(this, {
        'avgGrade': { get: function () { return this.grades.reduce((x, y) => x + y) / this.grades.length; } },
        'fullName': { get: function () { return this.firstName + ' ' + this.lastName; },
            set: function (name) {
                let words = name.split(' ');
                this.firstName = words[0] || '';
                this.lastName = words[1] || '';
            }
        }
    });

    this.getInfo = function(){
        console.log(this.firstName + ' ' + this.lastName + ' has average grade ' + this.avgGrade);
    }
}

let st1 = new Student('Bob', 'Peterson', '12543', [4, 3, 6, 3]);

console.log(st1.avgGrade);
console.log(st1.fullName);

st1.fullName = 'John Brown';
console.log(st1.fullName);

