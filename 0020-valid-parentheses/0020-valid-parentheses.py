class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # input: s
        # output: valid or not
        # no other chars
        # empty string -> true
        # optimal
        # if char open bracket, push to stack
        # if close bracket, check if last element in stack is the open match for it
        # check the dictionary which has key close:open
        # if u reach end of string -> check if stack not empty -> false
        dict_bracket = {"}":"{", "]":"[", ")":"("}
        stack = []
        for i in range(len(s)):
            if s[i] not in dict_bracket:
                stack.append(s[i])
            else:
                if stack and stack[-1]==dict_bracket[s[i]]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


        