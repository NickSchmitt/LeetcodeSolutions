function fib(n: number): number {
    const memo = {};
    const dp = (n) => {
        if(n <= 1) return n
        if(n in memo) return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    }
  
    return dp(n)
};