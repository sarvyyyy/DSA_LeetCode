class Solution:
    def search(self, nums: List[int], target: int):
        flag = False
        for i in range(len(nums)):
            if nums[i]== target:
                return i
                flag = True
        if flag == False:
            return -1
            
        