class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCounter = {}
        for num in nums:
            if num not in numsCounter:
                numsCounter[num] = 1
            else:
                return True

        return False
        

