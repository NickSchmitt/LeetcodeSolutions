function fib(n: number, memo = {}): number {
    if(n <= 1) return n
    if(!(n in memo)){ 
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
    }    
    return memo[n]
};