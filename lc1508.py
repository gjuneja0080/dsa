class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        lp, rp = 0, 0
        total, subsum = 0, 0
        while lp <= rp:
            subsum += nums[rp]
            res.append(subsum)
            if rp == len(nums) - 1:
                lp += 1
                if lp != len(nums) - 1:
                    rp = lp
                else:
                    res.append(nums[lp])
                    break
                subsum = 0
            else:
                rp += 1
        
        res.sort()
        
        for i in range(left, right + 1):
            total += res[i-1]

        return total % ((10 ** 9) + 7)
