use std::collections::BTreeMap;

impl Solution {
    pub fn largest_unique_number(a: Vec<i32>) -> i32 {
        
        let mut map = BTreeMap::new();
        
        for num in a {
            *map.entry(num).or_insert(0) += 1;
        }

        map.into_iter()
            .rev()
            .skip_while(|(_,v)|v>&1)
            .map(|(k, _)| k)
            .next()
            .unwrap_or(-1)
    }
}