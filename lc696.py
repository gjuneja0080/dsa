class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        groups = [1]
        prev = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                groups[-1] += 1
            else:
                groups.append(count)
                count = 1
            prev = s[i]
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
