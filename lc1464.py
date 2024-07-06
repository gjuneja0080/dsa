class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)        
        num1 = -heapq.heappop(max_heap)
        num2 = -heapq.heappop(max_heap)
        return (num1 - 1) * (num2 - 1)
