class Solution:

    def encode(self, strs: List[str]) -> str:
        d = ""
        for x in strs:
            p = len(x)
            d += str(p)+"/"+x
        return d

    def decode(self, s: str) -> List[str]:
        a = 0
        d = []
        j=0
        while j < len(s):
            if s[j] == '/':
                p = int(s[a:j])
                d.append(s[j+1:j+p+1])
                j += p+1
                a = j
            else:
                j+=1
        return d

        
