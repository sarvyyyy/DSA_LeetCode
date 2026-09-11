class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j+1
                    found = False
                    while k< len(nums2):
                        if nums2[k]>nums1[i]:
                            res.append(nums2[k])
                            found = True
                            break
                        k+=1
                    if not found:
                        res.append(-1)
                    break
                                   
        return res