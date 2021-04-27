impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        
        if n < 0 {return false};
        
        let max_exponent = f64::from(i32::max_value()).log(3.0) as u32;
        let largest_power_of_three: i32 = 3i32.pow(max_exponent);
        
        n > 0 && largest_power_of_three % n == 0
        
    }
}