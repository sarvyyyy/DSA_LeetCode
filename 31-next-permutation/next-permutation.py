class Solution:
    def nextPermutation(self, nums: List[int]):
        j = len(nums)-2
        while j>=0 and nums[j]>=nums[j+1]:
            j-=1
        if j>=0:
            k = len(nums)-1
            while nums[k]<=nums[j]:
                k-=1

            nums[j],nums[k]=nums[k],nums[j]

        nums[j+1:] = reversed(nums[j+1:])