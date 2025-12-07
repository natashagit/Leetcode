class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # popped element is right operand
        # input: list of strings
        # output: evaluated value
        # stack to put all the numbers

        # loop through tokens
        # if token is a number push to stack
        # if its an operand then pop two elements from stack
        # evaluate value and push back onto stack
        # finally return stack[-1]
        stack = []
        for i in range(len(tokens)):
            if tokens[i]=="*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif tokens[i]=="+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif tokens[i]=="-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tokens[i]=="/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]