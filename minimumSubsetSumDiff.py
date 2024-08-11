def subsetSum(nums, target):
    dp = []
    for i in range(len(nums) + 1):
        dp.append([False] * (target + 1))
    
    for i in range(len(nums) + 1):
        dp[i][0] = True
    
    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                
    return dp
def get_minSubsetSumDiff(nums):
    target = sum(nums)
    mat = subsetSum(nums, target)
    rows = len(mat)
    last_row = mat[-1]

    min_diff = float('inf')
    for i in range((target//2), -1, -1):
        if last_row[i]:
            min_diff = target - (2 * i)
            break
    return min_diff
    
nums = [1, 6, 11, 5]
ans = get_minSubsetSumDiff(nums)
print(ans)
