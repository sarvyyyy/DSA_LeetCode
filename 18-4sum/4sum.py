class Solution:
    def fourSum(self, nums: List[int], target: int):
        nums.sort()
        res=[]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                
                while k<l:
                    s = nums[i]+nums[j]+nums[k]+nums[l]
                    if target>s:
                        k+=1
                    elif target<s:
                        l-=1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

        return res
