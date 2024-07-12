class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numset:
                count = 1
                while num + 1 in numset:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest
