class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # input: s and t
        # output: smallest substring of s which contains s

        # keep two hashmaps with freq of t elements and freq of window elements
        # keep have and need counts

        if t == "":
            return ""
        countT = {}
        window = {}
        for i in t:
            countT[i] = countT.get(i, 0)+1
        have, need = 0, len(countT)
        result = [-1,-1] # for [l, r]
        result_length = float("inf")
        l = 0
        for r in range(len(s)):
            window[s[r]]= window.get(s[r], 0)+1

            if s[r] in countT and window[s[r]]==countT[s[r]]:
                have+=1
            
            while have == need:
                # update result
                if (r-l+1)<result_length:
                    result = [l, r]
                    result_length=r-l+1
                # pop from left of window
                window[s[l]]-=1
                # if while removing we made it less than what it needed to be
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l, r = result[0], result[1]
        if result_length!=float("inf"):
            return s[l:r+1]
        return ""