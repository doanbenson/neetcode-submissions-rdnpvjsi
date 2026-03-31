class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        # 0 -> a, 0 -> b, 0 -> c... [1,2,1,0...] -> key in hashmap add str to values
        # if the next str has the same key, add the key to values
        for s in strs:
            compare = [0] * 26
            for c in s:
                compareVal = ord(c) - ord("a")
                 #e.g. 'h' - 'a' = 7
                compare[compareVal] += 1 
                #should create new hash key for dict
            tup_compare = tuple(compare)
            hmap[tup_compare].append(s)

        
        return list(hmap.values())
