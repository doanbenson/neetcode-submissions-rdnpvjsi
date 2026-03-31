class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        index = 0

        while index < len(chars):
            group_end = index

            while group_end < len(chars) and chars[group_end] == chars[index]:
                group_end += 1
            
            chars[writer] = chars[index]
            writer += 1
            group_size = group_end - index

            if group_size > 1:
                for digit in str(group_size):
                    chars[writer] = digit
                    writer += 1
            
            index = group_end
        
        return writer



