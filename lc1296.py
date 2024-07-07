class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        occ_dict = Counter(nums)        # O(n)
        minheap = list(occ_dict.keys())     #O(n)
        heapq.heapify(minheap)              #O(n)
        while minheap:                  # O(n) because we don't pop until all occurences of element are deleted from heap
            minval = minheap[0]     
            for i in range(k):
                if occ_dict[minval + i] > 0:    
                    occ_dict[minval + i] -= 1
                    if occ_dict[minval + i] == 0:
                        heapq.heappop(minheap)         # O(logu) where u is the unique elements in nums
                else:
                    return False
        return True
# Total TC: 3xO(n) + O(logk) = O(n) + O(kXn)xO(logu)
