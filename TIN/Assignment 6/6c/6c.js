'use strict';
function handle() {
    let result = document.getElementById("result");
    if (validateForm()) {
        result.textContent = document.getElementById("hourNum").value + ' hours is logged.';
    } else { result.textContent = '' }
}

function validateForm() {
    let flag = true;
    let email = document.getElementById("email");
    let hourNum = document.getElementById("hourNum");
    let error1 = document.getElementById("validate1");
    let error2 = document.getElementById("validate2");
    let re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!re.test(email.value)) {
        error1.textContent = 'Email address is not in proper format';
        email.style.background = 'yellow';
        email.style.color = '#242831';
        flag = false;
    } else {
        error1.textContent = '';
        email.style.background = 'transparent';
        email.style.color = '#fafbff';
    }
    if (hourNum.value === '') {
        error2.textContent = 'This field is required';
        hourNum.style.background = 'yellow';
        hourNum.style.color = '#242831';
        flag = false;
    } else {
        error2.textContent = '';
        hourNum.style.background = 'transparent';
        hourNum.style.color = '#fafbff';
    }
    return flag;
}
