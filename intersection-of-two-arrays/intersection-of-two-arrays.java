class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Set<Integer> compareSet = new HashSet<>(), intersectionSet = new HashSet<>();
        
        for(int i : nums1) compareSet.add(i);
        
        for(int i : nums2) if(compareSet.contains(i)) intersectionSet.add(i);
        
        return intersectionSet.stream().mapToInt(Number::intValue).toArray();
    }
}