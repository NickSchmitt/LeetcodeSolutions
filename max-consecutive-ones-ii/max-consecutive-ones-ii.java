class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int leftPointer = 0, rightPointer = 0, zeroes = 0, max=0;
        
        while (rightPointer < nums.length){
            if (nums[rightPointer] == 0){
                zeroes++;
            }
            
            if (zeroes > 1){
                if(nums[leftPointer]==0){
                    zeroes--;
                }
                leftPointer++;
            }
            
            max = Math.max(rightPointer-leftPointer+1, max);
            
            rightPointer++;
            
        }
        return max;
    }
}