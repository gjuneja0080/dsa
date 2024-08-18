class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        def lcstring(str1, str2, n, m):
            dp = []
            for i in range(n + 1):
                dp.append([0] * (m + 1))

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[m][n]
        return lcstring(s, rev_s, len(s), len(rev_s))
