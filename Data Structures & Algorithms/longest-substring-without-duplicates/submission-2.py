class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        left, right = 0, 1
        max_length = 0

        # "zxyzxyz"

        while right <= len(s):
            substr = s[left:right]
            hset = set(substr)
            if len(hset) == len(substr):
                max_length = max(max_length, len(substr))
                right += 1
            else:
                left += 1
        
        return max_length

                

