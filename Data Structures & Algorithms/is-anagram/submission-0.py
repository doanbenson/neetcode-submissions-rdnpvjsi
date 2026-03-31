class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_one = {}
        letters_two = {}

        for letters in s:
            if letters not in letters_one:
                letters_one[letters] = 1;
            else:
                letters_one[letters] += 1;
        
        for letters in t:
            if letters not in letters_two:
                letters_two[letters] = 1;
            else:
                letters_two[letters] += 1;

        if letters_one == letters_two:
            return True
        return False
        
