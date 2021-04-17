class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int j = 0, i = 0; j < s.length(); j++) {
            Character letter = s.charAt(j);
            if (map.containsKey(letter)) i = Math.max(map.get(letter), i);
            ans = Math.max(ans, j - i + 1);
            map.put(letter, j + 1);
        }
        return ans;
    }
}