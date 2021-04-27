class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int min = prices[0];
        
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

// class Solution {
//     public int maxProfit(int[] prices) {
//         int maxP = 0;
//         int min = prices[0];
        
//         for (int i = 0; i<prices.length; i++){
//             if(prices[i] < min) min = prices[i];
//             else if(prices[i] - min > maxP) maxP = prices[i] - min;
//         }
        
//         return maxP;
//     }
// }