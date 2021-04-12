class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        vector<int> v;
        
        for (int i = 0; i<nums.size(); i++){
            int newIndex = abs(nums[i])-1;
            if (nums[newIndex] > 0) nums[newIndex] *= -1;
        }
        for (int i = 1; i<=nums.size(); i++){
            if (nums[i-1] > 0) v.push_back(i);
        }
        return v; 
    }
};