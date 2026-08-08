/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let res = [];
    let n = arr.length;
    let i = 0;
    while (i<n){
        let upL = Math.min(i+size,n);
        let temp = arr.slice(i,upL);
        res.push(temp);
        i+=size;
    }
    return res;
};
