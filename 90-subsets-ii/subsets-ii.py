class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backTrack(start, path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backTrack(i+1, path)
                path.pop()
            
        backTrack(0, [])
        return res