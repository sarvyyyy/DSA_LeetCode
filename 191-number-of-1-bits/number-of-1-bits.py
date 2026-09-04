class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if 1 & (n>>i):
                count+=1
        return count