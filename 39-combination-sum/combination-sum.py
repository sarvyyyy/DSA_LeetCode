class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backTrack(i, path, candidates[i] + total)
                path.pop()

        backTrack(0, [], 0)
        return res