/**
 * @param {number[]} A
 * @return {number}
 */
var largestUniqueNumber = function(A) {
    map = {}
    for(let i of A){
        if (!map.hasOwnProperty(i)){
            map[i] = 1
        }else{
            map[i]++
        }
    }
    x = Object.keys(map).map(x=>parseInt(x)).filter(x => map[x] === 1)
    return x.length ? Math.max(...x) : -1
};