class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        res = [0] * len(nums)
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums)
        
        for idx, val in enumerate(nums):
            if zero_cnt:
                if val:
                    res[idx] = 0
                else:
                    res[idx] = prod
            else:
                res[idx] = prod // val
        return res