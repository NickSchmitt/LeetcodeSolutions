class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int counter = 0;
        int max = 0;
        for (int i : nums){
            if (i == 1){
                counter++;
                max = Math.max(counter, max);
            } else {
                counter = 0;
            }
        }
        return max;
    }
}