class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(path, i):
            if len(path) == len(digits):
                res.append(path)
                return
            for c in mappings[digits[i]]:
                dfs(path + c, i + 1)
        
        if digits:
            dfs("", 0)
        return res