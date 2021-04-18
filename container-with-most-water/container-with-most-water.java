class Solution {
    public int maxArea(int[] height) {
        
        int i = 0, j = height.length-1, ans = 0;
        
        while (i<j){
            int area = (j-i) * Math.min(height[i], height[j]);
            ans = Math.max(ans, area);
            if (height[i]<height[j]) i++;
            else if(height[j]<height[i]) j--;
            else{
                i++;
                j--;
            }
        }
        return ans;
    }
}