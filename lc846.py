class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        else:
            occdict = Counter(hand)
            min_heap = list(occdict.keys())
            heapq.heapify(min_heap)
            while min_heap:
                sub = []
                minval = min_heap[0]
                for i in range(groupSize):
                    if occdict[minval + i] > 0:
                        sub.append(minval + i)
                        occdict[minval + i] -= 1

                        if occdict[minval + i] == 0:
                            heapq.heappop(min_heap)

                if len(sub) != groupSize:
                    print(sub)
                    return False
            return True
