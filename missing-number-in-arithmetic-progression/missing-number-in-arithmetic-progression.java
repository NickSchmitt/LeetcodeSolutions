class Solution {
    public int missingNumber(int[] arr) {
        int minDiff = Math.abs(arr[0]-arr[1]); // 2
        int removed = arr[0];
        
        
        for (int i = 1; i < arr.length-1; i++){
            int currDiff = Math.abs(arr[i]-arr[i+1]); // 4
            if(minDiff < currDiff){
                return (arr[i]+arr[i+1])/2;
            }
            if(minDiff > currDiff){
                return (arr[i]+arr[i-1]) / 2;
            }
        }
        return removed;
    }
}