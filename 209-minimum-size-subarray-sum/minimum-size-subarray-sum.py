class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]):
        s = 0
        size = float('inf')
        left=0
        for right in range(len(nums)):
            s+=nums[right]
            while s>= target:
                s-=nums[left]
                size = min(size, right-left+1)
                left+=1
        return 0 if size==float('inf') else size