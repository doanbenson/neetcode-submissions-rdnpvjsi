class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            group = 1

            while group + i < len(chars) and chars[i] == chars[group + i]:
                group += 1
            
            chars[insert] = chars[i]
            insert += 1
            if group > 1:
                group_string = str(group)
                chars[insert: insert + len(group_string)] = list(group_string)
                insert += len(group_string)

            i += group

        return insert

        # ["a", "a", "a", "b", "c", "c"]
        # ["a", "3", "b", "c", "2", ignored "c"]

