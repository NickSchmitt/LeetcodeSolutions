/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    return ![...nums.reduce((acc, num) => {
        acc.has(num) ? acc.set(num, acc.get(num)+1) : acc.set(num, 1)
        return acc
    }, new Map()).values()].every(num => num == 1 || num == 0)
};