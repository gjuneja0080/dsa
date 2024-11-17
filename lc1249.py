class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        stack = []
        to_remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        to_remove.update(stack)
        for i in range(len(s)):
            if i not in to_remove:
                res += s[i]

        return res
