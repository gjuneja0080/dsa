class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        visited = set()
        m, n = len(nums1), len(nums2)
        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        
        while k > 0 and min_heap:
            val, (i, j) = heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            if ((i+1, j) not in visited) and i+1 < m:
                heappush(min_heap, (nums1[i+1] + nums2[j], (i + 1, j)))
                visited.add((i+1, j))

            if ((i, j+1) not in visited) and j+1 < n:
                heappush(min_heap, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
            k-=1
        return res
