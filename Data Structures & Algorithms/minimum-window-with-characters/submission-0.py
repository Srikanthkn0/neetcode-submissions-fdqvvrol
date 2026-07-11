class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT={}
        res,reslen=[-1,-1],float("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        for i in range(len(s)):
            countS = {}
            for j in range(i,len(s)):
                if j-i+1 >= reslen:
                    break
                countS[s[j]] = countS.get(s[j],0) + 1

                flag=True
                for c in countT:
                    if countT[c] > countS.get(c,0):
                        flag=False
                        break

                if flag:
                    reslen = j-i+1
                    res = [i,j]
                    break
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""