impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        use std::collections::HashMap;
        use std::cmp::max;
        
        let mut map: HashMap<char, i32> = HashMap::new();
        let mut i = 0;
        let mut longest = 0;
        
        for (j, char) in s.chars().enumerate(){
            if let Some(x) = map.get(&char){
                i = max(*map.get(&char).unwrap(), i);
            }
            longest = max(longest, j as i32-i+1);
            map.insert(char, j as i32 + 1);
        }
        
        longest
        
    }
}