class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        max_heap = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if len(max_heap) < k:
                    heapq.heappush(max_heap, (-(arr[i] / arr[j]), arr[i], arr[j]))
                else:
                    heapq.heappushpop(max_heap, (-(arr[i]/arr[j]), arr[i], arr[j]))
        
        frac, arri, arrj = heapq.heappop(max_heap)

        return [arri, arrj]
