class Solution {
    public int largestUniqueNumber(int[] A) {
        
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        int max = Integer.MIN_VALUE;
        
        for (int i : A){
            int x = (count.containsKey(i)) ? -1 : i;
            count.put(i, x);
        }
        
        for (int i : count.values()){
            max = Math.max(i, max);
        }
        return max;
        
        
    }
}