class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasher = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1 #creating the key 10100..1100 : [acts, pots]
            hasher[tuple(key)].append(s)
        
        return list(hasher.values())