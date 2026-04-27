class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            maxLength = k + 1
            maxFreq = 1
            counter = {s[0] : 1}

            l, r = 0, 1
            while r < len(s):
                counter[s[r]] = counter.get(s[r], 0) + 1
                maxFreq = max(maxFreq, counter[s[r]])
                r += 1

                while r - l - maxFreq > k:
                    counter[s[l]] -= 1
                    l += 1

                maxLength = max(maxLength, r - l)
            
            return maxLength
             