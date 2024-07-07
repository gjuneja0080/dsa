class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        occ = defaultdict(int)
        
        for i in nums:                  # Storing each element in dictionary means going through each item of nums. Time complexity: O(n)
            occ[i] += 1
        
        for num, occurence in occ.items():                  
            if len(max_heap) < k:
                heapq.heappush(max_heap, (occurence, num))              # TC: O(nlogk) where n is the number of unique elements
            else:
                heapq.heappushpop(max_heap, (occurence, num))           # TC: O(nlogk) where n is the number of unique elements
        
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])              #TC: O(klogk) where k is the number of times the loop runs and log k is the time it takes to pop the element
            
        return res

'''
Counting Frequencies: O(n)
Building the heap: O(n log k)
Extracting top k elements: O(k log k)
Total time complexity: O(n) + O(n logk) + O(k logk) = O(nlogk) as nlogk dominates O(n) and O(klogk)
'''
