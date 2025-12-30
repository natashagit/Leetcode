class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # input: s1 and s2
        # output: true/false if s1's permutation in s2
        
        # sliding window
        # keep a dict of freq of s1
        # keep i=0
        # loop through s2
        # store in substring dict of s2
        # if substring dict!= freq dict of s1-> substring dict[s[i]]-=1, i+=1 
        # if substring dict[s[i]]==0-> delete it

        freq_s1 = {}
        for i in s1:
            if i not in freq_s1:
                freq_s1[i]=1
            else:
                freq_s1[i]+=1
        i=0
        freq_s2 = {}
        
        for j in range(len(s2)):
            if s2[j] in freq_s2:
                freq_s2[s2[j]]+=1
            else:
                freq_s2[s2[j]]=1
            
            if j-i+1>len(s1):
                freq_s2[s2[i]]-=1
                if freq_s2[s2[i]]==0:
                    del freq_s2[s2[i]]
                i+=1
            if freq_s2==freq_s1 and len(freq_s1)==len(freq_s2):
                return True
        return False
