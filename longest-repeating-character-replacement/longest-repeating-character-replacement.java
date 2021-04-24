class Solution {
    public int characterReplacement(String s, int k) {

        char[] charArr = new char[26];

        int i = 0, longest = 0, modeCharCount = 0;

        for (int j = 0; j < s.length(); j++) {
            modeCharCount = Math.max(modeCharCount, ++charArr[s.charAt(j) - 'A']);
            while (j - i + 1 - modeCharCount > k) {
                charArr[s.charAt(i) - 'A']--;
                i++;
            }
            longest = Math.max(longest, j - i + 1);
        }

        return longest;
    }
}