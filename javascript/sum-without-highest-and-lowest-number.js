function sumArray(array) {
    if(array == null || array.length <= 2){
        return 0;              
    }
    else{
        array.sort(function(a, b){return a-b});
        array.shift();
        array.pop();
        return array.reduce((accumulator, currentValue) => accumulator + currentValue);
    };
}

console.log(sumArray([6, 2, 1, 8, 10]));

