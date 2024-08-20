class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        count, cur_element = 0, nums[0]
        for i in range(len(nums)):
            if nums[i] != cur_element:
                if count > n:
                    return cur_element
                else:
                    count = 1
                    cur_element = nums[i]
            else:
                count += 1
        return cur_element
