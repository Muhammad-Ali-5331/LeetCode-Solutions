/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let nA = [];
    for (let idx = 0; idx<arr.length; idx++){
        if (fn(arr[idx],idx)) nA.push(arr[idx]);
    }
    return nA;
};