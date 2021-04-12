class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        
        for (int i = 0;; i++){
            auto num = umap.find(target-nums[i]);
            
            if (num != umap.end())
                return vector<int> {i, num -> second};
            
            umap[nums[i]] = i;
        }
    }
};