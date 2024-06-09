class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(ind = 0, lst=[]):
            if ind >= len(s) and len(lst) == 4:
                res.append('.'.join(lst[:]))
                return
            for i in range(ind, len(s)):
                phrase = s[ind:i+1]
                if int(phrase) <= 255:
                    if len(phrase) > 1 and phrase[0] != '0':
                            lst.append(phrase)
                            backtrack(i + 1, lst)
                            lst.pop()
                    elif len(phrase) == 1:
                        lst.append(phrase)
                        backtrack(i + 1, lst)
                        lst.pop()
        res = []
        backtrack()
        return res
