class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        
        for s in strs:
            count = len(s)
            res.append(str(count) + "#" + s)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
       
        while start < len(s):
            count = start
            while s[count] != "#":
                count += 1
            length = int(s[start:count]) #end exclusive
            start = count + 1
            count = start + length
            res.append(s[start:count])
            start = count

        return res
            