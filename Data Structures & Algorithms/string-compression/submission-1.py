class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            counter = read

            while counter < len(chars) and chars[read] == chars[counter]:
                counter += 1
            
            group_size = counter - read
            chars[write] = chars[read]
            write += 1

            if group_size > 1:
                for digit in str(group_size):
                    chars[write] = digit
                    write += 1
            read = counter
        
        return write
