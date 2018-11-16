'use strict';

function Student(firstName, lastName, id, grades){
    this.firstName = firstName;
    this.lastName = lastName;
    this.id = id;
    this.grades = grades;

    this.getInfo = function(){
        let avgGrade = this.grades.reduce((x, y) => x + y) / this.grades.length;
        console.log(this.firstName + ' ' + this.lastName + ' has average grade ' + avgGrade);
    }
}

let st1 = new Student('Bob', 'Peterson', '12543', [4, 3, 6, 3]);

st1.getInfo();