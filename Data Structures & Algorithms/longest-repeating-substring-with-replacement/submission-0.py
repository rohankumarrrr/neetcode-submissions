class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left, right = 0, 1
        
        while (right <= len(s)):
            substr = s[left:right]
            counter = Counter(substr)
            most_common = max(counter, key=counter.get)
            if len(substr) - counter[most_common] <= k:
                max_len = max(len(substr), max_len)
                right += 1
            else:
                left += 1

        return max_len
            