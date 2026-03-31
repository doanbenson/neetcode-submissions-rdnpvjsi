class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCounter = {}
        for i in range(len(nums)):
            if target - nums[i] in numCounter:
                return [numCounter[target - nums[i]], i]
            else:
                numCounter[nums[i]] = i
