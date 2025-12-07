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
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t=='+':
                    stack.append(b+a)
                elif t=='*':
                    stack.append(b*a)
                elif t=='-':
                    stack.append(b-a)
                else:
                    stack.append(int(float(b)/a))
        if stack:
            return stack[-1]