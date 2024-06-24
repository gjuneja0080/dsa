class Solution:
    def scoreOfString(self, s: str) -> int:
        vals = [ord(i) for i in s]
        diffs = []
        for i in range(1, len(vals)):
            diffs.append(abs(vals[i] - vals[i-1]))
        return sum(diffs)

