// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function returnAnArray(){
    var arr = [];
    for(var i = 1; i <= 255; i++) {
        console.log(i);
        arr.push(i);
    }
    return arr;
}
returnAnArray();