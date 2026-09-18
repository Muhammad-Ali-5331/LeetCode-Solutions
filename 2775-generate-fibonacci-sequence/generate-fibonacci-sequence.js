/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    yield 0
    yield 1
    let n1 = 0;
    let n2 = 1;
    while (true){
        let res = n1 + n2;
        n1 = n2;
        n2 = res;
        yield res;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */