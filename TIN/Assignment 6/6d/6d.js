'use strict';

function handle(){
    if(!validateForm()){
        return;
    }
    let tb = document.getElementById('tb');
    let newRow = document.createElement('tr');
    let tableCells = [3];
    for (let i = 0; i < 3; i++){
        tableCells[i] = document.createElement('td');
        if(i < 2){
            tableCells[i].textContent = document.getElementById('field' + i).value;
        } else{
            let curDate = new Date();
            tableCells[i].textContent = new Date().toUTCString();
        }
        newRow.appendChild(tableCells[i]);
    }
    tb.appendChild(newRow);
    document.getElementById('field0').value = '';
    document.getElementById('field1').value = '';
}

function validateForm(){
    let field0 = document.getElementById("field0").value;
    let field1 = document.getElementById("field1").value;
    if(field0 === '' || field1 === ''){
        document.getElementById('error').textContent = "Invalid input";
        return false;
    } else{
        document.getElementById('error').textContent = "";
        return true;
    }
}
