class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: return -1
        lp, rp = 0, len(nums) - 1
        while lp <= rp:

            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[rp]:
                if nums[mid] < target <= nums[rp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            else:
                if nums[lp] <= target < nums[mid]:
                    rp = mid - 1
                else:
                    lp = mid + 1

        return -1