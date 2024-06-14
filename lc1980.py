class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ''
        binlist = ['0', '1']
        n = len(nums[0])
        
        def backtrack(bin_str):
            nonlocal res
            if len(bin_str) == n:
                if bin_str not in nums:
                    res = bin_str
                    return
                else:
                    return
            for i in binlist:
                backtrack(bin_str + i)
        
        backtrack('')
        return res
