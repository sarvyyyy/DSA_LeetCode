class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        x = -1
        for i in nums:
            if x==-1:
                x = i
            elif i==x:
                x=-1
        return x