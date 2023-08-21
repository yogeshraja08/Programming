class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numarr=[]
        for i in s:
            try :
                a=int(i)
            finally:
                numarr.append(a)
        for i in numarr:
            if numarr[i]>=numarr[i+1]:
                return False
        return True

s = input()
obj = Solution()
res = obj.areNumbersAscending(s)
print(res)