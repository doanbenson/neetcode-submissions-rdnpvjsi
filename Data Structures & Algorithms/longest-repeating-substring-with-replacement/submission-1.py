class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            length = (r + 1 - l) - max(count.values())
            
            if length > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r + 1 - l)
        
        return res
