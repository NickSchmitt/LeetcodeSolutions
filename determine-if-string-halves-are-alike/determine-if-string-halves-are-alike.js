/**
 * @param {string} s
 * @return {boolean}
 */
const halvesAreAlike = s => {
    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    let left = right = 0
    for(let i = 0; i<s.length; i++){
        if(vowels.includes(s[i])){
            i < s.length/2 ? left++ : right++
        }
    }
    return left == right
};