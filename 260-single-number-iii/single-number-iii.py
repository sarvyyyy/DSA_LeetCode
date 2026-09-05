class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x = x ^ num
        mask = x & -x
        a = 0 
        b = 0
        for num in nums:
            if num & mask:
                a = a ^ num
            else:
                b = b ^ num
        return [a, b]