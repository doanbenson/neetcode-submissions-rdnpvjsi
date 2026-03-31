class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in counter:
                return [counter[diff], idx]
            counter[val] = idx  
        return []               