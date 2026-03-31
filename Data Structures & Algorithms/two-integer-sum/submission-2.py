class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}

        for idx, val in enumerate(nums):
            match = target - val 
            if match in num_idx:
                return [num_idx[match], idx]
            else:
                num_idx[val] = idx
        
        return []