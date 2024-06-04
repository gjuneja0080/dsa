class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lst = []
        res = []
        nums.sort()
        def backtrack(ind = 0):
            if ind == len(nums):
                res.append(lst[:])
                return

            lst.append(nums[ind])
            backtrack(ind + 1)
            lst.pop()

            while ind < len(nums) - 1 and nums[ind] == nums[ind + 1]: 
                ind += 1

            backtrack(ind + 1)
        
        backtrack()
        return res
