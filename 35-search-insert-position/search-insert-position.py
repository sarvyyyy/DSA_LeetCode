class Solution:
    def searchInsert(self, nums: List[int], target: int):
        if not nums:
            return 0

        n= len(nums)
        for i in range(n):
            if nums[i]== target:
                return i
                flag=True
        
        flag=False
        if flag==False:
            for j in range(n):
                if nums[j]>target:
                    return j
                    flag=True
                    break
                    
            return len(nums)