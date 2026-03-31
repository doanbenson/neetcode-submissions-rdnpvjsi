class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if window_count == key:
            return True

        for i in range(len(s1), len(s2)):
            window_count[s2[i]] += 1
            window_count[s2[i-len(s1)]] -= 1

            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            if window_count == key:
                return True
        return False