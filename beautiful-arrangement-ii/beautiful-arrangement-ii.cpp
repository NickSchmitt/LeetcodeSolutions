class Solution {
    public:
        vector<int> constructArray(int n, int k) {

            vector<int> ans(n);
            
            /* to create k differences, fill the vector from 1 ascending and k+1 descending
            e.g. k=3, 1, 4, 2, 3... */
            
            for (int i = 0, a = 1, z = k + 1; i <= k; i++)
                ans[i] = i % 2 ? z-- : a++;
            
            /* fill the rest of the vector with the remaining 1 to n elements in sequential order 
            e.g. n=6, ...5, 6 */
            
            for (int i = k+1; i < n; i++)
                ans[i] = i + 1;
            
            // ans = [1, 4, 2, 3, 5, 6], k = 3
            
            return ans;      
        }
};