class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                diff = target - total
                if abs(diff) < abs(target - closest):
                    closest = total

                    
                if diff>0:
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif diff<0:
                    k-=1
                else:
                    return target

        return closest       
                    
            