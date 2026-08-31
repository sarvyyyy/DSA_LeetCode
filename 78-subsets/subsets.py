class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(i, arr):
            if i==len(nums):
                ans.append(arr)
                return
            #don't take
            solve(i+1, arr)

            #take
            solve(i+1, arr+[nums[i]])

        solve(0,[])
        return ans