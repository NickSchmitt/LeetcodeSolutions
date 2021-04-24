class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int min = Integer.MAX_VALUE;
        
        for (int i = 0; i<prices.length; i++){
            min = Math.min(min, prices[i]);
            maxP = Math.max(maxP, prices[i]-min);
        }
        
        return maxP;
    }
}

/*

1,2,3,4,5

min = 1


*/