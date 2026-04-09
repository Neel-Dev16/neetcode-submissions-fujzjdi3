class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for i in details:
            ans=int(i[11:13])
            if ans>60:
                res+=1
        return res
        