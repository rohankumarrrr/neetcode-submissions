class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = dict()
        t_counter = dict()
        for i in range(0, len(s)):
            letter = s[i:i+1]
            if (letter in s_counter):
                s_counter[letter] = s_counter[letter] + 1
            else:
                s_counter[letter] = 1 
        for i in range(0, len(t)):
            letter = t[i:i+1]
            if (letter in t_counter):
                t_counter[letter] = t_counter[letter] + 1
            else:
                t_counter[letter] = 1 
        return (s_counter == t_counter)