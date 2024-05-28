class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num, min_num = str(num), str(num)
        to_rep = '0'
        prev = ''

        ind = 0
        while prev != '9':
            if ind == len(max_num): break
            if max_num[ind] != '9':
                prev = '9'
                to_rep = max_num[ind]
            ind += 1
            
        for num in max_num:
            if num == to_rep:
                max_num = max_num.replace(num, '9')
        
        ind = 0
        while prev != '0':
            if min_num[ind] != '0':
                prev = '0'
                to_rep = min_num[ind]
            ind += 1
        for num in min_num:
            if num == to_rep:
                min_num = min_num.replace(num, '0')
        
        return int(max_num) - int(min_num)
            
