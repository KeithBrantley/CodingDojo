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

// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

function sumOfAllEvenNumbers(){
    for(var i = 1; i <= 1000; i++) {
        if(i%2 == 0){
            sum.push(i);
            console.log(i);
        }
    }
    
}