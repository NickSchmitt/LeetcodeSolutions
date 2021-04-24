class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        int product = 1, count = 0, i = 0;
        for (int j = 0; j < nums.length; j++) {
            product *= nums[j];
            while (product >= k) product /= nums[i++];
            /* 
            the number of contiguous subarrays created by increasing window size
            is always equal to the length of the new window size
            [5, 2] -> [5,2,6] creates [5, 2, 6], [2, 6], [6]
            = 3 = new length = j-i+1
            */
            count += j - i + 1;
        }
        return count;
    }
}