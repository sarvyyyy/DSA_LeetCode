class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backTrack(start, path, total):
            if path in res:
                return

            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backTrack(i+1, path, candidates[i] + total)
                path.pop()

        backTrack(0, [], 0)

        return res