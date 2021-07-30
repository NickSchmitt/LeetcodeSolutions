class Solution(object):
    def countBinarySubstrings(self, s):
        
        ans, prev_count, cur_count = 0, 0, 1            # init cur_count at 1 to represent the first number
        
        for i in range(1, len(s)):                      # begin iterating at the 2nd number
            if s[i-1] != s[i]:
                ans += min(prev_count, cur_count)       # if sequence broken, the longest balanced sequence will be the lesser of the two
                prev_count, cur_count = cur_count, 1    # store the count of the most recent in prev, and init curr at 1 again
            else:
                cur_count += 1

        return ans + min(prev_count, cur_count)         # when we get to the end, do the calculation one more time