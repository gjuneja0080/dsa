class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        
        s.append(" ")
        lp = 0
        for i in range(len(s)):
            if s[i] == ' ':
                rp = i - 1
                while lp < rp:
                    s[lp], s[rp] = s[rp], s[lp]
                    lp += 1
                    rp -= 1
                lp = i + 1
        s.pop()
