/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    
    let prefix = ""
    
    if (strs.length == 0) return prefix
    
    //iterate over first word
    for (let i=0; i< strs[0].length; i++){
        
        // iterate over other words
        for (let j = 1; j<strs.length; j++){
            
            /*  
                if any of the words at the current index 
                don't match the first word's letter at the current index
                then return the prefix that's been built so far
            */  
            if(strs[j][i] !== strs[0][i]) return prefix
        }
        
        /* 
            if we get through the inner for loop that means all the words' current letters match
            so we can add the current character to the prefix
        */
        prefix = prefix+strs[0][i]
    }
    
    /*
        if we get through the outer for loop, we've made it through
        the entire first word while successfully matching all the other words
        which is the longest possible prefix, since the first word has no other
        letters, so it is itself the longest prefix
        
    */
    
    return prefix
   
    
    
};