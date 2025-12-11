class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        if n ==0:
            return 0
        size = 1
        s1 = ''
        for right in range(n):
            while s[right] in s1:
                s1 = s1[1:]
            s1+=s[right]
            size = max(size, len(s1))
        return size

        