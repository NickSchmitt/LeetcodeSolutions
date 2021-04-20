class Solution {
    
    private Map<Character, String> map = 
        Map.of('2', "abc", '3', "def", '4', "ghi", '5', "jkl", '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");
    
    private List<String> res = new LinkedList<String>();
    
    private String phoneDigits;
    
    public List<String> letterCombinations(String digits) {
        
        if (digits.length() == 0) return res;
        phoneDigits = digits;
        dfs(new StringBuilder(), 0);
        return res;        
    }
    
    private void dfs(StringBuilder path, int i){
        if (path.length() == phoneDigits.length()){
            res.add(path.toString());
            return;
        }
        
        String digitLetters = map.get(phoneDigits.charAt(i));
        for (char letter : digitLetters.toCharArray()){
            path.append(letter);
            dfs(path, i+1);
            path.deleteCharAt(path.length()-1);
            
        }
    }
}