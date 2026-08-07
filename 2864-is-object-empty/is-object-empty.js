/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    return Object.keys(obj).length === 0
    let l = obj.length ?? Object.keys(obj).length;
    if (l === 0) return true;
    if (l > 0) return false;
};