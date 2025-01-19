class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_dict={}
        for string in strs:
            str_key = "".join(sorted(string))
            if str_key in map_dict:
                map_dict[str_key].append(string)
            else:
                map_dict[str_key]= [string]
        return list(map_dict.values())
            

