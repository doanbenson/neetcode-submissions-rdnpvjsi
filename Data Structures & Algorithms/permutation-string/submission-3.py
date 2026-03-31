class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = Counter(s1)
        l, r = 0, len(s1)

        while r <= len(s2):
            window = Counter(s2[l:r])
            if window == key:
                return True
            l, r = l + 1, r + 1
        
        return False