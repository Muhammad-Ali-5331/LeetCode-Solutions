/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var localN = n;
    return function() {
        return localN++;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */