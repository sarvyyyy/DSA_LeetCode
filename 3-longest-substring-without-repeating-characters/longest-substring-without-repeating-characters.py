class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        left=0
        window = set()
        if n ==0:
            return 0
        size = 1
        for right in range(n):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            size = max(size, right-left+1)
        return size