class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # input: chars array
        # output: length of compressed string with each char+count of char if>1 to be appended
        # ["a","a","b","b","c","c","c"]
        # ["a","2","b","2","c","3","c"] -> 6
        insert = 0
        i=0
        while i<len(chars):
            group = 1
            while (group+i)<len(chars) and chars[group+i]==chars[i]:
                group+=1
            chars[insert] = chars[i] 
            insert+=1
            if group>1:
                string = str(group)
                chars[insert:insert+len(string)] = list(string)
                insert += len(string)
            i+=group
        return insert

        

        
