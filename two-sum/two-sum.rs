impl Solution { 
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
        use std::collections::HashMap;
        
        let mut hash: HashMap<i32,i32>= HashMap::new();
        
        for (i, num) in nums.iter().enumerate(){
            match hash.get(num) {
                Some(&x) => return vec![x, i as i32],
                None => hash.insert(target - num, i as i32)
            };
        }
        vec![]
    }    
}