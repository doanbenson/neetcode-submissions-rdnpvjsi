class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index: int, curr: List[int], total:int):
            if total == target:
                res.append(curr.copy())
                return
            
            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    return
                curr.append(nums[i])
                dfs(i, curr, total + nums[i])
                curr.pop()

        dfs(0, [], 0)
        return res