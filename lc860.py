class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        note_counter = defaultdict(int)
        for bill in bills:
            if bill == 5:
                note_counter[5] += 1
            elif bill == 10:
                if note_counter[5] > 0:
                    note_counter[5] -= 1
                    note_counter[10] += 1
                else:
                    return False
                    
            elif bill == 20:
                if note_counter[5] > 0 and note_counter[10] > 0:
                    note_counter[5] -= 1
                    note_counter[10] -= 1
                    note_counter[20] += 1

                elif note_counter[5] >= 3:
                    note_counter[5] -= 3
                    note_counter[20] += 1

                else:
                    return False
        return True
