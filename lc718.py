class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = []
        maxlen = 0
        n, m = len(nums1), len(nums2)
        for i in range(n + 1):
            dp.append([0] * (m + 1))
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i-1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                maxlen = max(maxlen, dp[i][j])

        return maxlen
