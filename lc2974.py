import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heapq.heapify(nums)
        while nums:
            bob_choice = heapq.heappop(nums)
            if nums:
                alice_choice = heapq.heappop(nums)
                arr.append(alice_choice)
                arr.append(bob_choice)
        return arr
