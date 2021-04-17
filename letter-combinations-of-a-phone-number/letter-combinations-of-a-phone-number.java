class Solution {
    
    //Array to return
    private List<String> combinations = new ArrayList<>();
    
    // Map of numbers and letters
    private Map<Character, String> letters = 
        Map.of('2', "abc", '3', "def", '4', "ghi", '5', "jkl", '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");
    
    // init copy of digits for backtrack function scope
    private String phoneDigits;
    
    // recursive function adds to combinations array
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return combinations;
        phoneDigits = digits;
        backtrack(0, new StringBuilder());
        return combinations;
    }
    
    
    private void backtrack(int index, StringBuilder path) {
        // add complete path to combinations array
        if (path.length() == phoneDigits.length()) {
            combinations.add(path.toString());
            return;
        }
        
        // create the path by adding a letter from each digit
        String possibleLetters = letters.get(phoneDigits.charAt(index));
        for (char letter: possibleLetters.toCharArray()) {
            path.append(letter);
            backtrack(index + 1, path);
            path.deleteCharAt(path.length() - 1);
        }
    }    
}