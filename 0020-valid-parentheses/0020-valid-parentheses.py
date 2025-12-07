class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # input: string of brackets
        # output: True/False if every open bracket has a closed one
        # stacks
        # dict -> save relationships ')':'('
        # loop through string
        # check if char in values
            # if so then add to stack
        # if not
            # check if stack empty
                # if empty-> return False
                # if not->check if dict[char] is stack.pop
                    # if not-> return False
        # if stack is empty
            # return True
        dict_brack = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in dict_brack.values():
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                else:
                    if dict_brack[char]==stack[-1]:
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True

                    