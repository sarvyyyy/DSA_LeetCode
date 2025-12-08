class Solution:
    def search(self, nums: List[int], target: int):
        
        if(target not in nums):
            return -1
        if(target in nums):
            return nums.index(target)