class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[]
        path=path.split("/")
        print(path)
        for p in path:
            if p=="" or p==".":
                continue
            if p=="..":
                if res:
                    res.pop()
            else:
                res.append(p)
        return "/" + "/".join(res)