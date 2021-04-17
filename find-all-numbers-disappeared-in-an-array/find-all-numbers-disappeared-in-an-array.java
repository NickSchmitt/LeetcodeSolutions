class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        List<Integer> missingIntegers = new LinkedList<Integer>();

        
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            nums[index] = -Math.abs(nums[index]);
        }
        
        

        for (int i = 1; i <= nums.length; i++) {
            if (nums[i - 1] > 0) missingIntegers.add(i);
        }
        
        return missingIntegers;
    }
}