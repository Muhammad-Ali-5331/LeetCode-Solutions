/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    let n = this.length;
    return n === 0 ? -1 : this[n-1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */