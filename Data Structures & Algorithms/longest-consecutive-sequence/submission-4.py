class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0

        for num in num_set:
            if num - 1 not in num_set:
                seq = 0
                while num + seq in num_set:
                    seq += 1
                length = max(seq, length)
        return length

