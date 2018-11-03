function binSearch(arr, value) {
    let start = 0,
        stop = arr.length - 1,
        half = Math.floor((start + stop) / 2);

    while (arr[half] !== value && start < stop) {
        if (value < arr[half]) {
            stop = half - 1;
        } else {
            start = half + 1;
        }
        half = Math.floor((start + stop) / 2);
    }

    return arr[half] !== value ? -1 : half;
}

let arr = [2, 5, 8, 9, 13, 45, 67, 99];
console.log(binSearch(arr, 45));