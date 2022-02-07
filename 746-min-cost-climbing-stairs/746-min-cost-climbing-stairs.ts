function minCostClimbingStairs(cost: number[]): number {
    const memo = {}
    const dp = (step) => {
        if(step <= 1) return 0
        if(!(step in memo)){
            memo[step] = Math.min(cost[step-1] + dp(step-1), cost[step-2] + dp(step-2))
        }
        return memo[step]
    }
    const topStep = cost.length
    return dp(topStep)
};

// [1,100,1]
/*



*/