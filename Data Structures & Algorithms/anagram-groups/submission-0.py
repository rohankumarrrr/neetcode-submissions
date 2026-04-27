from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)
        for index, word in enumerate(strs):
            sorted_word = ''.join(sorted(word))
            output_dict[sorted_word].append(word)
        output = []
        for key in output_dict:
            output.append(output_dict[key])
        return output
