impl Solution {
    pub fn replace_elements(mut arr: Vec<i32>) -> Vec<i32> {
        
        let mut max = -1;
        
        for num in arr.iter_mut().rev(){
            let current = *num;
            *num = max;
            max = current.max(max);
        }
        arr
    }
}