class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapped = {
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
        combination = []

        def dfs(i):
            if i == len(digits):
                if combination:
                    res.append(''.join(combination.copy()))
                return
            letters = mapped[digits[i]]
            for j in range(len(letters)):
                combination.append(letters[j])
                dfs(i + 1)
                combination.pop()

        dfs(0)
        return res

