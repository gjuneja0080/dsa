class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            dp = []
            n = len(nums)
            targetsum = total // 2
            for i in range(n + 1):
                dp.append([False] * (targetsum + 1))
            
            for i in range(n + 1):
                dp[i][0] = True
            
            for i in range(1, n + 1):
                for j in range(1, targetsum + 1):
                    if j < nums[i - 1]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]

            if dp[n][targetsum] == True:
                return True
