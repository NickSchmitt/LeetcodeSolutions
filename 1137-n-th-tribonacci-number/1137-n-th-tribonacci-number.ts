function tribonacci(num: number, memo = {}): number {
    if(num<=2) return num ? 1 : 0
    if(memo[num]) return memo[num]
    memo[num] = tribonacci(num-1, memo) + tribonacci(num-2, memo) + tribonacci(num-3, memo)
    return memo[num]
};