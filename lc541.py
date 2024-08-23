class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for start in range(0, len(s), 2 * k):
            s[start:start + k] = reversed(s[start:start + k])
        return ''.join(s)
