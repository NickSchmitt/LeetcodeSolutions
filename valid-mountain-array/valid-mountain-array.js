/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    
    let len = arr.length
    let i = 0
    
    // increment i until the peak, signified by either the array's end or the rise's end
    while (i+1 < len && arr[i] < arr[i+1]) i++
    
    // if the peak is first or last, can't be mountain as a mountain requires lesser elements after the peak
    if (i == 0 || i == len-1) return false
    
    // increment i until either the end or a value is not greater than the next value
    while (i+1 < len && arr[i] > arr[i+1]){
        i++
    }
    
    // it is a mountain array if the above condition satisfies all remaining elements
    return i == len-1
    
};