class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        occdict = defaultdict(int)
        for i in magazine:
            occdict[i] += 1
        for i in ransomNote:
            occdict[i] -= 1
            if occdict[i] < 0:
                return False
        return True
