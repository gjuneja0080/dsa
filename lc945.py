class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            original = nums[i]
            nums[i] = max(nums[i], nums[i-1] + 1)
            if original != nums[i]:
                count += abs(original - nums[i])
        return count
