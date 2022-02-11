function tribonacci(n: number): number {
    const memo = {};
    const dp = (num) => {
        if(num<=2) return num ? 1 : 0
        if(memo[num]) return memo[num]
        memo[num] = dp(num-1) + dp(num-2) + dp(num-3)
        return memo[num]
    }
    return dp(n)
};