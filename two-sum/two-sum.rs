impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        
        let mut map = HashMap::new();
        
        for (i, num) in nums.iter().enumerate() {
            
            match map.get(num){
                Some(&num) => return vec![num, i as i32],
                None => map.insert(target-num, i as i32)
            };
        }
        vec![]
    }
}