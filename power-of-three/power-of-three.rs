impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {

        // max_power_of_three = 3^⌊log_3(max_int)⌋ = 1162261467
        // powers of three divide by lesser powers of three without remainder
        
        n > 0 && 1162261467 % n == 0
        
    }
}