class Solution:
    def searchRange(self, nums: List[int], target: int):
        result =[0,0]
        flag = False
        first = False
        second = False
        for i in range(len(nums)):
            if first == False:
                if nums[i]==target:
                    result[0] = i
                    flag = True
                    first = True
            else:
                if nums[i]==target:
                    result[1] = i
                    second = True
            
        if first == True and second == False:
            result[1] = result[0]
        if flag == False and first == False:
            return[-1,-1]
        
        return result
        