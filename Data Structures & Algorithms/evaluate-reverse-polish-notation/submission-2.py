class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif ch=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif ch=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif ch=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(ch))
        return stack[0]