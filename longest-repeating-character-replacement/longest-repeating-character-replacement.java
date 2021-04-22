class Solution {
    public int characterReplacement(String s, int k) {
        /*
        Store letter counts in an array
        Store the mode count
        If non-mode characters in the window exceed k, shrink the window
        */
        
        int[] arr = new int[26];
        int mode = 0, left = 0, longest = 0;
        
        for(int right = 0; right < s.length(); right++){

            arr[s.charAt(right) - 'A']++;
            mode = Math.max(mode, arr[s.charAt(right) - 'A']);
            
            if(right - left + 1 - mode > k){
                arr[s.charAt(left) - 'A']--;
                left++;
            }
            
            longest = Math.max(longest, right - left + 1);
        }
        
        return longest;
    }
}