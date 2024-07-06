class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        score_dict = defaultdict(list)
        for stud, score in items:
            if len(score_dict[stud]) < 5:
                heapq.heappush(score_dict[stud], score)
            else:
                heapq.heappushpop(score_dict[stud], score)
        
        for stud, scores in score_dict.items():
            res.append([stud, int(sum(scores)/len(scores))])
        
        return sorted(res, key = lambda x: x[0])
