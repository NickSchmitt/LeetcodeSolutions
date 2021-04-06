/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    
    let max = -1
    
    for (let i = arr.length-1; i >= 0; i--){
        current = arr[i]
        arr[i] = max
        max = Math.max(current, max)
    }
    return arr
    
};