class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def countSubsets(nums, t):
            dp = []
            for i in range(len(nums)+1):
                dp.append([0] * (t + 1))
            for i in range(len(nums) + 1):
                dp[i][0] = 1
            for i in range(1, len(nums) + 1):
                for j in range(1, t + 1):
                    if j < nums[i-1]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-nums[i-1]]
            return dp[len(nums)][t]
        return countSubsets(coins, amount)
