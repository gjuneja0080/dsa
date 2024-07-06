class Solution:
    def frequencySort(self, s: str) -> str:
        occurences = {}
        inverted_occurences = defaultdict(list)
        for char in s:
            if char in occurences:
                occurences[char] += 1
            else:
                occurences[char] = 1
        
        for char, occ in occurences.items():
            inverted_occurences[occ].append(char)

        max_heap = []
        for key in inverted_occurences.keys():
            heapq.heappush(max_heap, -key)
        
        res = ''
        while max_heap:
            occurence = -heapq.heappop(max_heap)
            for char in inverted_occurences[occurence]:
                res += char * occurence

        return res
