class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list_res = list()
        for i in range(len(nums)-1):
            if((i > 0) and (nums[i] == nums[i-1])):
                continue
            temp_list = list()
            leftp, rightp = i+1, len(nums) - 1
            while(leftp < rightp):
                threesum = nums[i] + nums[leftp] + nums[rightp]
                if(threesum > 0):
                    rightp-=1
                elif(threesum < 0):
                    leftp+=1
                else:
                    list_res.append([nums[i], nums[leftp], nums[rightp]])
                    leftp+=1
                    while((nums[leftp] == nums[leftp-1]) and (leftp < rightp)):
                        leftp+=1
        return list_res
