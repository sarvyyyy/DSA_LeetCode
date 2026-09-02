class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def checkPal(s):
            return s == s[::-1]

        def backTrack(start, path):
            if start == len(s):
                res.append(path.copy())
                return

            for i in range(start, len(s)):
                substring = s[start:i+1]
                if checkPal(substring):
                    path.append(substring)
                    backTrack(i+1, path)
                    path.pop()
            
        backTrack(0, [])
        return res



