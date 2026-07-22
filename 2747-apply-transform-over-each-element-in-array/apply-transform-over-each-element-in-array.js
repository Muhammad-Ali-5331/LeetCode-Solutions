/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArr = [];
    for (let idx = 0; idx<arr.length; idx++){
        newArr.push(fn(arr[idx],idx));
    }
    return newArr;
};