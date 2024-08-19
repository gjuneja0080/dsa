class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sp = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[sp]:
                continue
            else:
                sp += 1
                nums[sp] = nums[i]

        return sp + 1
