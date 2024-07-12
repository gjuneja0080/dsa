class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(input_str, remphrase):
            stack = []
            for char in input_str:
                if (char == remphrase[1] 
                        and stack 
                        and stack[-1] == remphrase[0]):
                        stack.pop()
                else:
                    stack.append(char)

            return ''.join(stack)

                
        if x <= y:
            first_removal = "ba"
            second_removal = "ab"
        else:
            first_removal = "ab"
            second_removal = "ba"
        
        slist = list(s)
        total_score = 0

        modified_str = remove_substring(s, first_removal)
        pairs_removed = (len(s) - len(modified_str)) // 2
        total_score += pairs_removed * max(x, y)

        new_modified = remove_substring(modified_str, second_removal)
        pairs_removed = (len(modified_str) - len(new_modified)) // 2
        total_score += pairs_removed  * min(x, y)

        return total_score
