class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        st = []
        res = []
        for nums in nums2:
            while st and nums > st[-1]:
                mp[st.pop()] = nums
            st.append(nums)

        while st:
            mp[st.pop()] = -1
        for i in nums1:
            res.append(mp[i])
        return res
