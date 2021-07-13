/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle.length == 0) return 0
    
    let window = needle.length
    
    for (let i = 0; i<haystack.length; i++){
        if (needle == haystack.slice(i,window+i)){
            return i
        }
    }
    return -1
};