class Solution {
public String removeDuplicates(String s, int k) {
    
    // mutable char sequence
    StringBuilder string = new StringBuilder(s);
    
    // stack for tracking char repetition counts
    Stack<Integer> counts = new Stack<>();
    
    for (int i = 0; i < string.length(); ++i) {
        // if newly encountered char, add new count to stack
        if (i == 0 || string.charAt(i) != string.charAt(i - 1)) {
            counts.push(1);
        // else increment repetition count. 
        } else {
            int curr = counts.pop() + 1;
            // if k in a row, remove all from char sequence. 
            if (curr == k) {
                string.delete(i - k + 1, i + 1);
                i = i - k;
            } else {
                counts.push(curr);
            }
        }
    }
    return string.toString();
}
};