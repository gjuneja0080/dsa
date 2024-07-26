class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        occ_dict = defaultdict(int)
        for num in nums:
            occ_dict[num] += 1
        if k == 0:
            for num, occ in occ_dict.items():
                if occ > 1:
                    count += 1
        else:
            for num, occ in occ_dict.items():
                if num + k in occ_dict:
                    count += 1
        return count
