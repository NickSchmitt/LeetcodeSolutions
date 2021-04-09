class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        end = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[end]:
                end += 1
                nums[end] = nums[i]
        return end + 1