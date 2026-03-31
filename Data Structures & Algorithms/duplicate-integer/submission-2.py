class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCounter = {}
        for n in nums:
            if n not in numCounter:
                numCounter[n] = 1
            else:
                return True
        return False