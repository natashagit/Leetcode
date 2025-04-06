class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i]=='*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif tokens[i]=='-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tokens[i]=='+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif tokens[i]=='/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]