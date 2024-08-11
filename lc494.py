class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #target is the diff
        total = sum(nums)
        diff = target
        if (diff + total) % 2 != 0 or total < abs(target): return 0
        new_target = (diff + total) // 2
        dp = []
        for i in range(len(nums) + 1):
            dp.append([0] * (new_target + 1))
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(new_target + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]

        return dp[len(dp)-1][new_target]
