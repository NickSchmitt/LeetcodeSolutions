var partitionLabels = function(s) {
    // iterate string
    
    // track first and last position of each letter
    
    // where none of the last positions overlap with first positions, create partition
    
    // return size of each partition
    
    let map = {}
    
    // a -> start, end
    
    for (let i = 0; i<s.length; i++){
        let letter = s[i]
        if (letter in map){
            map[letter] = [map[letter][0], i]
            
        } else {
            map[letter] = [i, i]
        }
    }
    
    let res = []
    let currentPartition = [-1, -1]
    
    for (let [start, end] of Object.values(map)){
        
        if (start > currentPartition[1]){
            
            res.push(currentPartition[1] - currentPartition[0] + 1)
            currentPartition = [start, end]
        } else if (end > currentPartition[1]){
            currentPartition[1] = end
        }
        
        // either update the current partition or start a new one
        
            // if 
    }
    res.push(currentPartition[1] - currentPartition[0] + 1)
    
    return res.slice(1)
    
    /*
    a start = 0
    
    a end = 8
    
    b end < a end
    c end < a end
    
    partition end = a end
    
    d start = 9
    
    */
    
};