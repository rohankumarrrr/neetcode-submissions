class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '@*/'
        elif strs == [""]:
            return '@*/@*/'
        
        return "@*/".join(s for s in strs)

    def decode(self, s: str) -> List[str]:
        if s == '@*/':
            return []
        elif s == '@*/@*/':
            return [""]
        
        return s.split("@*/")
