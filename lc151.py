class Solution:
    def reverseWords(self, s: str) -> str:
        res = []

        for i in range(len(s)):
            if s[i] == " " and len(res) == 0:
                continue
            elif s[i] == " " and len(res) > 0:
                if res[-1] != " ":
                    res.append(s[i])
                else:
                    continue
            else:
                res.append(s[i])

        ans = "".join(res)
        lst = ans.split(' ')
        
        while lst[-1] == "":
            lst.pop()

        return " ".join(lst[::-1])
