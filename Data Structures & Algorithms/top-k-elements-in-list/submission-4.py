from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if not n in count:
                count[n] = 1
            else:
                count[n] += 1
        
        # Input: nums = [1,2,2,3,3,3], k = 2
        # count: {1: 1, 2: 2, 3: 3}

        freq = [[] for i in range(len(nums) + 1)]
        # freq[i] = x, where i is the number of times x appears in nums
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res = []
        for bucket in freq[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []
        

    
    



    

