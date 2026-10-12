class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        # print(s)
        # print(t)
        if s != t:
            return False
        for i in range(len(s)):
            print(s[i],t[i])
            if s[i] != t[i]:
                return False
        return True
        

# RACECAR
# 0123456
# CARRACE
# 4560123
# 4443333

            
        