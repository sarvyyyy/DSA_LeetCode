class Solution:
    def searchRange(self, nums: List[int], target: int):
        def findFirst():
            idx = -1
            left = 0
            right = len(nums)-1
            while right>=left:
                mid = (right+left) // 2
                if nums[mid]<=target:
                    left = mid+1
                else:
                    right = mid-1
                if nums[mid]==target:
                    idx = mid
            return idx

        def findLast():
            left = 0
            idx = -1
            right = len(nums)-1
            while left<=right:
                mid = (right+left) // 2
                if nums[mid]>=target:
                    right = mid-1
                else:
                    left = mid+1
                if target == nums[mid]:
                    idx = mid
            return idx
        return [findLast(), findFirst()]
