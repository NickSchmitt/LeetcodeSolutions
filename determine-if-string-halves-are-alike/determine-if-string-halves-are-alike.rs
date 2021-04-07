impl Solution {
    pub fn halves_are_alike(string: String) -> bool {
        let vowels = "aeiouAEIOU".to_string();
        let mut left = 0;
        let mut right = 0;
        for (index, char) in string.chars().enumerate(){
            if vowels.contains(char) {
                if index < string.len()/2 { left+=1 }
                else{ right += 1}
            }
        }
        left == right
    }
}