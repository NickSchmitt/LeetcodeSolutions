/**
 * @param {number[]} A
 * @return {boolean}
 */
var isIdealPermutation = function(A) {
    for (let i = 0; i < A.length-1; i++){
        if(A[i] > i+1) return false
        if(A[i] > A[i+1]){
            if(A[i] > (A[i+1]+1)) return false
            i++
        }
    }
    return true 
};