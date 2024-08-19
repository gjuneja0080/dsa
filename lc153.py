class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] < nums[rp]:
                rp = mid
            elif nums[mid] > nums[rp]:
                lp = mid + 1
            else:
                return nums[mid]
