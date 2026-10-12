class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False
        # # s = sorted(s)
        # # t = sorted(t)
        # # for i,j in zip(s,t):
        # #     if i!=j:
        # #         return False
        # # return True
        # cnts,cntt = {},{}
        # for a,b in zip(s,t):
        #     cnts[a] = cnts.get(a,0)+1
        #     cntt[b] = cntt.get(b,0)+1
        # return cnts == cntt

        # k = int(len(s))
        # for x in s:
        #     if x in t:
        #         k = k - 1
        # return k==0 and len(s)==len(t)
        # return sorted(s) == sorted(t)
        # s = sorted(s)
        # t = sorted(t)
        # # print(s)
        # # print(t)
        # if s != t:
        #     return False
        # for i in range(len(s)):
        #     print(s[i],t[i])
        #     if s[i] != t[i]:
        #         return False
        # return True
        

# RACECAR
# 0123456
# CARRACE
# 4560123
# 4443333

            
        