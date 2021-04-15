class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        for (int i = 0; i<nums.length; i++){
            
            // Math.abs to counteract negative marker if num encountered multiple times.
            // subtracting one to match index with value
            int newIndex = Math.abs(nums[i])-1;
            
            // mark number at position with negative to ensure the number has been seen 
            if (nums[newIndex] > 0){
                nums[newIndex] *= -1;
            }
        }
        
        List<Integer> result = new LinkedList<Integer>();
        
        // if it's still positive we haven't seen it
        for (int i = 1; i <= nums.length; i++){
            if (nums[i-1] > 0){
                result.add(i);
            }
        }
        
        return result;
    }
}