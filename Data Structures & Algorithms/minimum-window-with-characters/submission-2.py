class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = Counter(t), {}
        l = 0
        minLength = float("inf")
        have, need = 0, len(t_count)
        res_index = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t and window[c] == t_count[c]:
                have += 1
            while have == need:
                length = r - l + 1
                if length < minLength:
                    res_index = [l, r]
                    minLength = length
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res_index
        if minLength == float("inf"):
            return ""
        return s[l: r + 1]