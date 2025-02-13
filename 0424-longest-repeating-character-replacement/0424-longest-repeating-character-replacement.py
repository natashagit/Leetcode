class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Time Complexity = O(n)
        start = 0
        count = {}
        max_count = 0
        max_length = 0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            max_count = max(max_count, count[s[i]])
            if (i-start+1)-max_count>k:
                count[s[start]]-=1
                start+=1
            max_length = max(max_length, i-start+1)
        return max_length

        # Brute Force approach: Time Complexity= O(n^2)
        # maxlen=0
        # for i in range(len(s)):
        #     d = {}
        #     maxf = 0
        #     for j in range(i, len(s)):
        #         if s[j] in d:
        #             d[s[j]]+=1
        #         else:
        #             d[s[j]]=1
        #         maxf = max(maxf, d[s[j]])
        #         # Len - maxfreq: can be changed
        #         changes = (j-i+1)-maxf
        #         if changes<=k:
        #             maxlen = max(maxlen, j-i+1)
        #         else:
        #             break
        # return maxlen




        