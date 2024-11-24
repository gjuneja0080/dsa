class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_unmatched = 0
        close_unmatched = 0

        for char in s:
            if char == '(':
                open_unmatched += 1
            elif char == ')':
                if open_unmatched > 0:
                    open_unmatched -= 1
                else:
                    close_unmatched += 1
        return open_unmatched + close_unmatched
        
