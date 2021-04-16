class Solution {
    
    // init memo
    private Map<Integer, Integer> memo = new HashMap<>();
    
    
    public int fib(int n) {
        
        // base case + handle fib(0)
        if (n <= 1) return n;
        
        // check memo for previously computed value
        if (memo.containsKey(n)) return memo.get(n);
        
        // if not in memo, compute, memoize, and return it
        int result = fib(n-1) + fib(n-2);
        memo.put(n, result);
        return result;
    }
}